{
  'target_defaults': {
    'include_dirs': [
      'include',
      'builds/gyp'
    ],
    'defines': [
      '_REENTRANT',
      '_THREAD_SAFE',
      'ZMQ_CUSTOM_PLATFORM_HPP',
      'ZMQ_GYP_BUILD',
      'ZMQ_CACHELINE_SIZE=64',
      'HAVE_STRNLEN',
      'ZMQ_USE_CV_IMPL_NONE'
    ],
    'conditions': [
      [ 'OS=="win"', {
        'defines': [
          'ZMQ_HAVE_WINDOWS',
          'ZMQ_STATIC',
          'FD_SETSIZE=16384',
          '_CRT_SECURE_NO_WARNINGS',
          '_WINSOCK_DEPRECATED_NO_WARNINGS'
        ],
        'libraries': [
          'ws2_32',
          'advapi32',
          'iphlpapi'
        ],
        'msvs_settings': {
          'VCCLCompilerTool': {
            'ExceptionHandling': '1',
            'AdditionalOptions': ['/EHsc']
          }
        }
      }],
      [ 'OS=="mac"', {
        'defines': [
          'ZMQ_HAVE_OSX'
        ]
      }],
      [ 'OS=="linux"', {
        'defines': [
          'ZMQ_HAVE_LINUX'
        ],
        'cflags_cc': [
          '-fvisibility=hidden',
          '-fexceptions'
        ],
        'cflags_cc!': [
          '-fno-exceptions',
          '-fno-rtti'
        ],
        'libraries': [
          '-lpthread'
        ]
      }]
    ],
  },
  'default_configuration': 'Debug',
  'configurations': {
    'Debug': {
      'defines': [ 'DEBUG', '_DEBUG' ],
      'cflags': [ '-Wall', '-Wextra', '-O0', '-g', '-ftrapv' ],
      'msvs_settings': {
        'VCCLCompilerTool': {
          'RuntimeLibrary': 1, # static debug
        },
      },
    },
    'Release': {
      'defines': [ 'NDEBUG' ],
      'cflags': [ '-Wall', '-Wextra', '-O3' ],
      'msvs_settings': {
        'VCCLCompilerTool': {
          'RuntimeLibrary': 0, # static release
        },
      },
    }
  },
  'targets': [
    {
      'target_name': 'libzmq',
      'type': 'static_library',
      'includes': [ 'zmq.gypi' ],
      'sources': [ '<@(zmqsources)' ],
      'copies': [{
        'destination': 'src',
        'files': [ 'builds/gyp/platform.hpp' ]
      }],
      'xcode_settings': {
        'GCC_ENABLE_CPP_RTTI': 'YES',
        'GCC_SYMBOLS_PRIVATE_EXTERN': 'YES',  # -fvisibility=hidden,
        'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'    # -fexceptions
      }
    }
  ]
}
