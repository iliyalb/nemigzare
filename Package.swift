// swift-tools-version: 6.1
// The swift-tools-version declares the minimum version of Swift required to build this package.

import PackageDescription

let package = Package(
    name: "nemigzare",
    dependencies: [
        .package(url: "https://github.com/vapor/vapor.git", from: "4.92.1")
    ],
    targets: [
        .executableTarget(
            name: "nemigzare",
            dependencies: [
                .product(name: "Vapor", package: "vapor")
            ],
            resources: [.copy("../Assets")]
        )
    ]
)
