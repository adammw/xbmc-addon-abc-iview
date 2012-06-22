ABC iView plugin for XBMC
================================

This plugin provides a simple list of available programs from the ABC iView 
web site, and allows you to stream them with.

The content is only available with Australia, or you can apparently use sites
like Unblock-US or your own VPN solution which terminates in with an AU IP 
address.

This plugin wouldn't be possible without the great work on python-iview from
Jeremy Visser.
https://jeremy.visser.name/2009/08/python-iview/

Thanks also for contributions from:
  * sdt (Stephen Thirlwall)

Installation
------------
This plugin is available as part of the XBMC CatchUp TV AU repository, but
you'll always find the latest version here.

Download the latest ZIP file from the downloads section, and put it into your
'addons' directory of XBMC. This will differ between platforms.

For Windows:
```
	%APPDATA%\XBMC\addons
```

For Linux:
```
	~/.xbmc/addons
```

For Mac:
```
	~/Library/Application Support/XBMC/addons
```

For AppleTV:
```
	/Users/frontrow/Library/Application Support/XBMC/addons
```

Issues
------

### AppleTV won't start program

AppleTV 2+ users have reported that programs will not start. This is due to
a broken librtmp.

Try downloading an updated librtmp.0.dylib from:
http://supercloudtv.com/librtmp.html

Extract the ZIP file, and push the file to your AppleTV (maybe use WinSCP for
Windows users) to: ```/Applications/XBMC.frappliance/Frameworks```

Through SSH (PuTTY for Windows users) type this:
```
chown mobile.mobile /Applications/XBMC.frappliance/Frameworks/librtmp.0.dylib
chmod a+x /Applications/XBMC.frappliance/Frameworks/librtmp.0.dylib
```

Reboot your AppleTV and it should work.

### Reporting an issue

For any issues or bug reports, please file them at the GitHub issues part of
this project:
https://github.com/andybotting/xbmc-addon-abc-iview/issues

Please include log output if possible, using Github Gist or Pastebin.com.

The location of your XBMC log file will depend on your platform.

For Windows:
```
   %APPDATA%\XBMC\temp\xbmc.log
```

For Linux:
```
   ~/.xbmc/temp/xbmc.log
```

For Mac:
```
   ~/Library/Application Support/XBMC/temp/xbmc.log
```

For AppleTV:
```
   /Users/frontrow/Library/Application Support/XBMC/temp/xbmc.log
```

Contact Me
----------
For anything else, you can contact me by email at andy#andybottng.com
