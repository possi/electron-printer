{
  'targets': [
    {
      "target_name": "action_after_build",
      "type": "none",
      "dependencies": [ "<(module_name)" ],
      "copies": [
        {
          "files": [ "<(PRODUCT_DIR)/<(module_name).node" ],
          "destination": "<(module_path)"
        }
      ]
    },
    {
      'target_name': 'node_printer',
      'sources': [
        'src/node_printer.cc',
        'src/node_printer_posix.cc',
        'src/node_printer_win.cc'
      ],
      'include_dirs' : [
        "<!(node -e \"require('nan')\")"
      ],
      'cflags_cc+': [
        "-Wno-cast-function-type"
      ],
      'conditions': [
        # common exclusions
        ['OS!="linux"', {'sources/': [['exclude', '_linux\\.cc$']]}],
        ['OS!="mac"', {'sources/': [['exclude', '_mac\\.cc|mm?$']]}],
        ['OS!="win"', {
          'sources/': [['exclude', '_win\\.cc$']]}, {
          # else if OS==win, exclude also posix files
          'sources/': [['exclude', '_posix\\.cc$']]
        }],
        # specific settings
        ['OS!="win"', {
          'cflags':[
            '<!(cups-config --cflags)'
          ],
          'ldflags':[
            '<!(cups-config --libs)'
            #'-lcups -lgssapi_krb5 -lkrb5 -lk5crypto -lcom_err -lz -lpthread -lm -lcrypt -lz'
          ],
          'libraries':[
            '<!(cups-config --libs)'
            #'-lcups -lgssapi_krb5 -lkrb5 -lk5crypto -lcom_err -lz -lpthread -lm -lcrypt -lz'
          ],
          'link_settings': {
              'libraries': [
                  '<!(cups-config --libs)'
              ]
           }
        }]
      ]
    }
  ]
}
