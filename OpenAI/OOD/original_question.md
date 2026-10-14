# Original Question: Design Persistent Key-Value Store

+1 more  
Hard  
Hash Table

Interview Stages  
Onsite  
Frequency  
Asked By  
OPENAI-icon  
Last Reported  
1 weeks ago

## AI Insights

You are designing a persistent key-value store that supports saving and restoring its data using a binary middleware medium. The system should store only string keys and string values and be able to serialize its entire state to a binary blob for durability across restarts.

A storage interface called Medium is provided, allowing you to save and retrieve a single binary blob. The implementation is in InMemoryMedium.

```java
// This is a provided API interface.
interface Medium {
    /**
     * Saves a byte array to the storage medium (e.g., file, in-memory).
     * @param data The byte array to persist.
     */
    void saveBlob(byte[] data);

    /**
     * Retrieves the most recently saved byte array from the storage medium.
     * @return The stored byte array, or null if nothing is saved.
     */
    byte[] getBlob();
}
```

You need to implement the KVStore class, ensuring that the binary serialization format can exactly recover all string keys and values, including those with Unicode characters or empty strings. Native object serialization (such as direct use of language-specific serialization, or JSON) is not allowed. You must construct your own serialization format.

## Implement the KVStore class

- `KVStore(Medium medium)` Initializes a new, empty key-value store using the provided storage medium. The store only interacts with data via this medium.
- `void put(String key, String value)` Stores the specified value associated with the given key. If the key already exists, its value is updated.
- `String get(String key)` Returns the value associated with key. If the key is not present, it returns the empty string `""`.
- `void shutdown()` Serializes the current store into a custom binary format and writes it to the associated medium. After shutdown, the instance becomes closed, any subsequent get or put must fail and throw an error.
- `void restore()` Loads the key-value data from the binary blob saved in the medium, completely replacing the in-memory store. If the blob is missing or empty, the store should become empty.

## Constraints

- Keys and values are arbitrary strings (may include Unicode and empty strings).
- After calling shutdown, the instance is permanently closed; further calls to get or put must fail.
- The restore method always replaces the in-memory state, discarding any unsaved changes.
- 1 ≤ number of keys ≤ 10⁴.
- Total size of all keys and values together ≤ 10⁶ characters.
- Each key and value is a string of length ≤ 10⁴.
- All methods are called in a valid order (e.g., shutdown is not called twice in a row).

## Example

**Input:**

```text
["InMemoryMedium", "KVStore", "put", "put", "put", "get", "get", "shutdown", "KVStore", "get", "put", "restore", "get", "get", "get", "get"]
[[], [], ["key1", "value1"], ["key2", "value2_is_longer"], ["key3", "value3"], ["key1"], ["key4"], [], [medium], ["key1"], ["key4", "value4"], [], ["key1"], ["key2"], ["key3"], ["key4"]]
```

**Output:**

```text
[null, null, null, null, null, "value1", "", null, null, "", null, null, "value1", "value2_is_longer", "value3", ""]
```

**Explanation:**

```java
Medium medium = new InMemoryMedium();
KVStore store1 = new KVStore(medium); // Initializes a new store backed by medium.
store1.put("key1", "value1"); // Stores "key1" -> "value1".
store1.put("key2", "value2_is_longer"); // Stores "key2" -> "value2_is_longer".
store1.put("key3", "value3"); // Stores "key3" -> "value3".
store1.get("key1"); // Returns "value1".
store1.get("key4"); // Returns "".
store1.shutdown(); // Persists the current store and closes this instance.
KVStore store2 = new KVStore(medium); // Creates a new store with same medium.
store2.get("key1"); // Returns "", since nothing has been restored yet.
store2.put("key4", "value4"); // Adds "key4" -> "value4" to store2's in-memory map.
store2.restore(); // Loads the blob, replacing all in-memory data with what was persisted by store1.
store2.get("key1"); // Returns "value1", loaded from persisted state.
store2.get("key2"); // Returns "value2_is_longer".
store2.get("key3"); // Returns "value3".
store2.get("key4"); // Returns "", since "key4" was never persisted and was overwritten by restore.
```
