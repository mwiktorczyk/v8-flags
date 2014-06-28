{
  'targets': [
    {
      'target_name': 'v8_flags',
      'sources': [
         'src/v8_flags.cc'
      ],
      'include_dirs': [
        '<!(node -e "require(\'nan\')")',
        '<!(node -e \'console.log(require("path").join(process.env.HOME, ".node-gyp", process.versions.node, "src"))\')',
        '<!(node -e \'console.log(require("path").join(process.env.HOME, ".node-gyp", process.versions.node, "deps", "v8", "src"))\')'
      ]
    },
    {
      'target_name': 'v8_flag_definitions',
      'sources': [
         'src/v8_flag_definitions.cc'
      ],
      'include_dirs': [
        '<!(node -e "require(\'nan\')")',
        '<!(node -e \'console.log(require("path").join(process.env.HOME, ".node-gyp", process.versions.node, "src"))\')',
        '<!(node -e \'console.log(require("path").join(process.env.HOME, ".node-gyp", process.versions.node, "deps", "v8", "src"))\')'
      ],
      'cflags_cc': [ '-Wno-comment' ]
    }
  ]
}
