#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-shell-extensions
Version  : 3.26.1
Release  : 9
URL      : https://download.gnome.org/sources/gnome-shell-extensions/3.26/gnome-shell-extensions-3.26.1.tar.xz
Source0  : https://download.gnome.org/sources/gnome-shell-extensions/3.26/gnome-shell-extensions-3.26.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: gnome-shell-extensions-data
Requires: gnome-shell-extensions-locales
BuildRequires : gettext
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gio-2.0)

%description
GNOME Shell Extensions is a collection of extensions providing additional
and optional functionality to GNOME Shell.

%package data
Summary: data components for the gnome-shell-extensions package.
Group: Data

%description data
data components for the gnome-shell-extensions package.


%package locales
Summary: locales components for the gnome-shell-extensions package.
Group: Default

%description locales
locales components for the gnome-shell-extensions package.


%prep
%setup -q -n gnome-shell-extensions-3.26.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507153299
%configure --disable-static --enable-extensions=all --disable-classic-mode
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1507153299
rm -rf %{buildroot}
%make_install
%find_lang gnome-shell-extensions

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/glib-2.0/schemas/org.gnome.shell.extensions.auto-move-windows.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.shell.extensions.example.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.shell.extensions.native-window-placement.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.shell.extensions.screenshot-window-sizer.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.shell.extensions.user-theme.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.shell.extensions.window-list.gschema.xml
/usr/share/gnome-shell/extensions/alternate-tab@gnome-shell-extensions.gcampax.github.com/convenience.js
/usr/share/gnome-shell/extensions/alternate-tab@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/alternate-tab@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/alternate-tab@gnome-shell-extensions.gcampax.github.com/prefs.js
/usr/share/gnome-shell/extensions/alternate-tab@gnome-shell-extensions.gcampax.github.com/stylesheet.css
/usr/share/gnome-shell/extensions/apps-menu@gnome-shell-extensions.gcampax.github.com/convenience.js
/usr/share/gnome-shell/extensions/apps-menu@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/apps-menu@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/apps-menu@gnome-shell-extensions.gcampax.github.com/stylesheet.css
/usr/share/gnome-shell/extensions/auto-move-windows@gnome-shell-extensions.gcampax.github.com/convenience.js
/usr/share/gnome-shell/extensions/auto-move-windows@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/auto-move-windows@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/auto-move-windows@gnome-shell-extensions.gcampax.github.com/prefs.js
/usr/share/gnome-shell/extensions/auto-move-windows@gnome-shell-extensions.gcampax.github.com/stylesheet.css
/usr/share/gnome-shell/extensions/drive-menu@gnome-shell-extensions.gcampax.github.com/convenience.js
/usr/share/gnome-shell/extensions/drive-menu@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/drive-menu@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/drive-menu@gnome-shell-extensions.gcampax.github.com/stylesheet.css
/usr/share/gnome-shell/extensions/example@gnome-shell-extensions.gcampax.github.com/convenience.js
/usr/share/gnome-shell/extensions/example@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/example@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/example@gnome-shell-extensions.gcampax.github.com/prefs.js
/usr/share/gnome-shell/extensions/example@gnome-shell-extensions.gcampax.github.com/stylesheet.css
/usr/share/gnome-shell/extensions/launch-new-instance@gnome-shell-extensions.gcampax.github.com/convenience.js
/usr/share/gnome-shell/extensions/launch-new-instance@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/launch-new-instance@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/launch-new-instance@gnome-shell-extensions.gcampax.github.com/stylesheet.css
/usr/share/gnome-shell/extensions/native-window-placement@gnome-shell-extensions.gcampax.github.com/convenience.js
/usr/share/gnome-shell/extensions/native-window-placement@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/native-window-placement@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/native-window-placement@gnome-shell-extensions.gcampax.github.com/stylesheet.css
/usr/share/gnome-shell/extensions/places-menu@gnome-shell-extensions.gcampax.github.com/convenience.js
/usr/share/gnome-shell/extensions/places-menu@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/places-menu@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/places-menu@gnome-shell-extensions.gcampax.github.com/placeDisplay.js
/usr/share/gnome-shell/extensions/places-menu@gnome-shell-extensions.gcampax.github.com/stylesheet.css
/usr/share/gnome-shell/extensions/screenshot-window-sizer@gnome-shell-extensions.gcampax.github.com/convenience.js
/usr/share/gnome-shell/extensions/screenshot-window-sizer@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/screenshot-window-sizer@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/screenshot-window-sizer@gnome-shell-extensions.gcampax.github.com/stylesheet.css
/usr/share/gnome-shell/extensions/user-theme@gnome-shell-extensions.gcampax.github.com/convenience.js
/usr/share/gnome-shell/extensions/user-theme@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/user-theme@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/user-theme@gnome-shell-extensions.gcampax.github.com/stylesheet.css
/usr/share/gnome-shell/extensions/window-list@gnome-shell-extensions.gcampax.github.com/convenience.js
/usr/share/gnome-shell/extensions/window-list@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/window-list@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/window-list@gnome-shell-extensions.gcampax.github.com/prefs.js
/usr/share/gnome-shell/extensions/window-list@gnome-shell-extensions.gcampax.github.com/stylesheet.css
/usr/share/gnome-shell/extensions/windowsNavigator@gnome-shell-extensions.gcampax.github.com/convenience.js
/usr/share/gnome-shell/extensions/windowsNavigator@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/windowsNavigator@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/windowsNavigator@gnome-shell-extensions.gcampax.github.com/stylesheet.css
/usr/share/gnome-shell/extensions/workspace-indicator@gnome-shell-extensions.gcampax.github.com/convenience.js
/usr/share/gnome-shell/extensions/workspace-indicator@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/workspace-indicator@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/workspace-indicator@gnome-shell-extensions.gcampax.github.com/prefs.js
/usr/share/gnome-shell/extensions/workspace-indicator@gnome-shell-extensions.gcampax.github.com/stylesheet.css

%files locales -f gnome-shell-extensions.lang
%defattr(-,root,root,-)

