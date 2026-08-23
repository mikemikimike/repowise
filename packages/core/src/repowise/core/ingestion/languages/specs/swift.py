"""LanguageSpec for swift (extracted from the registry data table)."""

from ..spec import LanguageSpec

SPEC = LanguageSpec(
    tag="swift",
    display_name="Swift",
    # Live-validated on Alamofire @ 7595cbc: intra-module type edges,
    # SPM target mapping, @main entry detection — 0% orphans, 0.70 resolution.
    import_support="full",
    # XCTest/SPM conventions: FooTest(s).swift; Tests/ root is a generic token.
    test_camel_suffixes=("Test", "Tests"),
    entry_point_patterns=("main.swift", "App.swift"),
    extensions=frozenset({".swift"}),
    grammar_package="tree_sitter_swift",
    scm_file="swift.scm",
    heritage_node_types=frozenset(
        {"class_declaration", "protocol_declaration", "extension_declaration"}
    ),
    manifest_files=("Package.swift",),
    builtin_calls=frozenset(
        {
            "print",
            "debugPrint",
            "fatalError",
            "precondition",
            "assert",
            "min",
            "max",
            "abs",
            "stride",
            "zip",
            "map",
            "filter",
            "reduce",
            "sorted",
        }
    ),
    builtin_parents=frozenset(
        {
            "NSObject",
            "Codable",
            "Encodable",
            "Decodable",
            "Hashable",
            "Equatable",
            "Comparable",
            "CustomStringConvertible",
            "Error",
            "Sendable",
        }
    ),
    # Standard-library and Foundation type names. Read only by the bare-name
    # fallback, to stop `Data(contentsOf:)` binding to a repository's
    # `extension Data`: an extension can add members to one of these types but
    # does not own the initializer the call site named.
    #
    # Selected by rust's rule, a name a repository plausibly declares in its own
    # right stays off, which is why `Result`, `Error`, `Task`, `Operation`,
    # `Request` and `Response` are absent. Constructors only; no bare method
    # names, because type construction is the whole measured population.
    #
    # `OperationQueue` came off on measurement: Alamofire declares a real
    # `convenience init` on it in an extension and the call site invokes that
    # one, so listing the name deleted a correct edge. That is the ceiling here,
    # a name match cannot see whether the extension it refuses declares the
    # initializer being called. Upgrade path is a symbol-shaped test, not a
    # longer list.
    builtin_methods=frozenset(
        {
            # Foundation value types
            "Data", "URL", "URLRequest", "URLResponse", "HTTPURLResponse",
            "URLComponents", "URLQueryItem", "URLSession", "URLSessionConfiguration",
            "UUID", "Date", "DateComponents", "DateFormatter", "ISO8601DateFormatter",
            "NumberFormatter", "IndexPath", "IndexSet", "CharacterSet",
            "Bundle", "Locale", "TimeZone", "Calendar", "FileManager",
            "JSONDecoder", "JSONEncoder", "JSONSerialization",
            "PropertyListDecoder", "PropertyListEncoder",
            "NotificationCenter", "ProcessInfo", "RunLoop", "Thread",
            "DispatchQueue", "DispatchGroup", "DispatchSemaphore", "DispatchTime",
            "InputStream", "OutputStream", "Pipe",
            "NSNumber", "NSString", "NSError", "NSNull", "NSLock", "NSRecursiveLock",
            # Stdlib containers and scalars
            "Array", "Dictionary", "Set", "String", "Substring", "Character",
            "Int", "Int8", "Int16", "Int32", "Int64",
            "UInt", "UInt8", "UInt16", "UInt32", "UInt64",
            "Double", "Float", "Bool", "Range", "ClosedRange",
        }
    ),
    color_hex="#F05138",
)
