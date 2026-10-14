def encode(text):
    # text -> blob
    # len(text)+text
    byte_text=text.encode("utf-8")
    byte_len=len(byte_text).to_bytes(4,"big")
    return byte_len+byte_text

def decode(blob,offset):
    # blob -> text, offset
    byte_len=blob[offset:offset+4]
    length=int.from_bytes(byte_len,"big")
    offset+=4

    byte_text=blob[offset:offset+length]
    text=byte_text.decode("utf-8")
    offset+=length
    return text,offset

import struct
from abc import ABC, abstractmethod
from io import BytesIO

# The Medium interface allows persisting and retrieving raw binary data.
class Medium(ABC):
    @abstractmethod
    def saveBlob(self, data):
        pass

    @abstractmethod
    def getBlob(self):
        pass

# An in-memory implementation of the Medium interface for testing purposes.
class InMemoryMedium(Medium):
    def __init__(self):
        self.storage = None

    def saveBlob(self, data):
        self.storage = data

    def getBlob(self):
        return self.storage

class KVStore:
    def __init__(self, medium):
        # TODO: Implement __init__ logic.
        self.medium=medium
        self._data={} # key:value
        self.closed=False

    def put(self, key, value):
        # TODO: Implement put logic.
        if self.closed:
            raise RuntimeError
        self._data[key]=value

    def get(self, key):
        # TODO: Implement get logic.
        if self.closed:
            raise RuntimeError
        return self._data.get(key,"")

    def shutdown(self):
        # TODO: Implement shutdown logic.
        if self.closed:
            raise RuntimeError

        #num_pairs + encode(k)+encode(value)
        num_pairs=len(self._data)
        blobs=[num_pairs.to_bytes(4,"big")]
        for k in self._data:
            blobs.append(encode(k))
            value=self._data[k]
            blobs.append(encode(value))

        self.medium.saveBlob(b"".join(blobs))
        self.closed=True
        return 
        

    def restore(self):
        # TODO: Implement restore logic.
        self._data={}

        blobs=self.medium.getBlob()
        if blobs is None or len(blobs)<4:
            return self._data
        num_pairs=int.from_bytes(blobs[:4])
        offset=4
        for i in range(num_pairs):
            key,offset=decode(blobs,offset)
            value,offset=decode(blobs,offset)
            self._data[key]=value
        return self._data
        

    @staticmethod
    def main(args):
        KVStore.test1()
        KVStore.test2()
        KVStore.test3()

    @staticmethod
    def test1():
        print("===== Test 1 =====")

        medium = InMemoryMedium()
        store1 = KVStore(medium)
        store1.put("key1", "value1")
        store1.put("key2", "value2_is_longer")
        store1.put("key3", "value3")
        print(store1.get("key1"))  # Expected: "value1"
        print(store1.get("key4"))  # Expected: ""
        store1.shutdown()

        store2 = KVStore(medium)
        print(store2.get("key1"))  # Expected: ""
        store2.put("key4", "value4")

        store2.restore()
        print(store2.get("key1"))  # Expected: "value1"
        print(store2.get("key2"))  # Expected: "value2_is_longer"
        print(store2.get("key3"))  # Expected: "value3"
        print(store2.get("key4"))  # Expected: ""

    @staticmethod
    def test2():
        print("\n===== Test 2 =====")

        medium = InMemoryMedium()
        store1 = KVStore(medium)
        store1.put("counter", "1")
        store1.put("status", "active")
        print(store1.get("counter"))  # Expected: "1"
        print(store1.get("status"))  # Expected: "active"
        store1.shutdown()

        store2 = KVStore(medium)
        store2.restore()
        store2.put("counter", "2")
        store2.put("status", "inactive")
        store2.put("new_field", "added")
        print(store2.get("counter"))  # Expected: "2"
        print(store2.get("status"))  # Expected: "inactive"
        print(store2.get("new_field"))  # Expected: "added"
        store2.shutdown()

        store3 = KVStore(medium)
        store3.restore()
        print(store3.get("counter"))  # Expected: "2"
        print(store3.get("status"))  # Expected: "inactive"
        print(store3.get("new_field"))  # Expected: "added"

    @staticmethod
    def test3():
        print("\n===== Test 3 =====")

        medium = InMemoryMedium()
        store1 = KVStore(medium)
        store1.put("emoji_key_😊", "emoji_value_🎉")
        store1.put("unicode_key_中文", "unicode_value_日本語")
        store1.put("empty_value", "")
        print(store1.get("emoji_key_😊"))  # Expected: "emoji_value_🎉"
        print(store1.get("empty_value"))  # Expected: ""
        store1.shutdown()

        store2 = KVStore(medium)
        store2.restore()
        print(store2.get("emoji_key_😊"))  # Expected: "emoji_value_🎉"
        print(store2.get("unicode_key_中文"))  # Expected: "unicode_value_日本語"
        print(store2.get("empty_value"))  # Expected: ""
        print(store2.get("nonexistent_key"))  # Expected: ""

if __name__ == "__main__":
    KVStore.main([])
