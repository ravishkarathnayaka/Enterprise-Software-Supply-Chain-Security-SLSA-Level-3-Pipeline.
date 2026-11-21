package supplychain.licenses

default allow = false

allowed_licenses := {
    "Apache-2.0",
    "MIT",
    "BSD-2-Clause",
    "BSD-3-Clause",
    "ISC",
    "Python-2.0",
}

allow if {
    count(violating_licenses) == 0
}

violating_licenses contains pkg if {
    some pkg in input.packages
    not allowed_licenses[pkg.license]
}
