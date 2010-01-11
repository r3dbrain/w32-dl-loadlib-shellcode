build_config = {
  "version": "0.1",
  "projects": {
    "w32-dl-loadlib-shellcode-hash-list.asm": {                               # List of hashes
      "files": {
        "w32-dl-loadlib-shellcode-hash-list.asm": {
          "sources": ["w32-dl-loadlib-shellcode-hash-list.txt"],
          "build commands": [
              ["hash\\hash.cmd",
                "--input=w32-dl-loadlib-shellcode-hash-list.txt",
                "--output=w32-dl-loadlib-shellcode-hash-list.asm"],
          ],
        },
      },
    },
    "w32-dl-loadlib-shellcode.bin": {
      "architecture": "x86",
      "dependencies": ["w32-dl-loadlib-shellcode-hash-list.asm"],
      "files": {
        "w32-dl-loadlib-shellcode.bin": {
          "sources":  ["w32-dl-loadlib-shellcode.asm"],
          "includes": ["w32-dl-loadlib-shellcode-hash-list.asm"],
        },
      },
    },
    "w32-dl-loadlib-shellcode-esp.bin": {
      "architecture": "x86",
      "dependencies": ["w32-dl-loadlib-shellcode-hash-list.asm"],
      "files": {
        "w32-dl-loadlib-shellcode-esp.bin": {
          "sources":  ["w32-dl-loadlib-shellcode.asm"],
          "includes": ["w32-dl-loadlib-shellcode-hash-list.asm"],
          "defines":  {"STACK_ALIGN": "TRUE"},
        },
      },
    },
  },
  "test commands": ["test-w32-dl-loadlib-shellcode.cmd"],
}
