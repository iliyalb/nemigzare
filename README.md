# nemigzare

![App window](Assets/sample.png?raw=true)

## About

Bouncing DVD logo screen saver in form of a web app.

## Why

Swift of all things, and on Linux too?!

> DISCLAIMER: SwiftUI is not available on Linux, this code is using Vapor (Apple WebKit framework)

![Reason](Assets/why.png?raw=true)

<b>WHY NOT</b>

## Requirements

Debian:

```sh
curl -L https://swiftlygo.xyz/install.sh | bash
```

Arch:

```sh
paru -S swift-bin
```

## Build and run

Install the dependencies:

```sh
swift package resolve
```

Serve the app:

```sh
swift build && swift run
```

By default the server starts on [http://127.0.0.1:8080](http://127.0.0.1:8080)

## License

This is free and unencumbered software released into the public domain under The Unlicense.

Anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means.

See [UNLICENSE](LICENSE) for full details.
