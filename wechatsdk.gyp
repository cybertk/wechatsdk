# Copyright 2013 (c) Kyan <kyan.ql.he@gmail.com>
{
  'targets': [
    {
      'target_name': 'wechatsdk',
      'type': 'none',

      'conditions': [
        ['OS == "ios"', {
          'link_settings': {
            'libraries': [
              '$(SDKROOT)/System/Library/Frameworks/Foundation.framework',
              'libWeChatSDK_armv7_armv7s.a',
            ],
          } # end link_settings
        }],  # end, OS == "ios"
      ],
    },  # target 'wechatsdk'
  ],
}
