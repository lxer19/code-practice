---
topic: ood
patterns:
  - persistence
  - serialization
  - key-value-store
companies:
  - OpenAI
status: solved
---

# Persistent Key-Value Store

## Pattern

An in-memory string dictionary with whole-store snapshot persistence through a Medium that saves and retrieves one binary blob. The serialization format is defined explicitly rather than using native object serialization.

## Key constraints

- Keys and values are arbitrary strings, including Unicode and empty strings.
- A new instance starts empty and does not automatically restore saved data.
- `put` updates an existing key; `get` returns an empty string for a missing key.
- `shutdown` saves the snapshot and permanently closes the instance; later `get` and `put` calls must fail.
- `restore` replaces the current data, discarding unsaved changes. A missing or empty blob produces an empty store.
- JSON and native object serialization are not allowed.
- The stated limits are at most 10⁴ keys, 10⁴ characters per key or value, and 10⁶ characters across all keys and values.

## My initial mistakes

## Core insight

The notebook documents a length-prefixed format: a 4-byte entry count, followed by each key and value as a 4-byte unsigned big-endian byte length and its UTF-8 payload. Lengths count encoded bytes rather than characters. Decoding advances an offset after each length field and payload; an empty string naturally has a payload length of zero.

The restored dictionary replaces the current dictionary, and restoring data must not reopen an instance that has been permanently closed.

## Follow-up variants

The notebook lists these questions for further practice:

- How should truncated blobs, invalid lengths, and invalid UTF-8 be handled?
- What should happen to the closed state if saving fails?
- What guarantees should Medium provide if the process crashes during a save?
- How should multiple instances or threads accessing the data behave?
- How could persistence be extended when the data is too large to save the entire snapshot each time?

These notes summarize the existing [question](question.md) and [practice notebook](practice.ipynb).
