workspace "HelloWorld"
    configurations {"Debug", "Release"}

project "HelloWorld"
    location "HelloWorld"
    kind "ConsoleApp"
    language "C++"
    targetdir "bin/%{cfg.buildcfg}"

    files { "HelloWorld/src/**.h", "HelloWorld/src/**.cpp" }

    filter "configurations:Debug"
        defines {"Debug"}
        symbols "On"

    filter "configurations:Release"
        defines {"NDEBUG"}
        optimize "On"