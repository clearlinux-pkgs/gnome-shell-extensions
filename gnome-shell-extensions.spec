#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-shell-extensions
Version  : 3.28.1
Release  : 13
URL      : https://download.gnome.org/sources/gnome-shell-extensions/3.28/gnome-shell-extensions-3.28.1.tar.xz
Source0  : https://download.gnome.org/sources/gnome-shell-extensions/3.28/gnome-shell-extensions-3.28.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: gnome-shell-extensions-data
Requires: gnome-shell-extensions-locales
BuildRequires : meson
BuildRequires : ninja
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : python3

%description
GNOME Shell Sass is a project intended to allow the sharing of the theme sources in sass between gnome-shell and other projects like gnome-shell-extensions.

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
%setup -q -n gnome-shell-extensions-3.28.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1524726062
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain   builddir
ninja -v -C builddir

%install
DESTDIR=%{buildroot} ninja -C builddir install
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
/usr/share/gnome-shell/extensions/drive-menu@gnome-shell-extensions.gcampax.github.com/convenience.js
/usr/share/gnome-shell/extensions/drive-menu@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/drive-menu@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/drive-menu@gnome-shell-extensions.gcampax.github.com/stylesheet.css
/usr/share/gnome-shell/extensions/launch-new-instance@gnome-shell-extensions.gcampax.github.com/convenience.js
/usr/share/gnome-shell/extensions/launch-new-instance@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/launch-new-instance@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/launch-new-instance@gnome-shell-extensions.gcampax.github.com/stylesheet.css
/usr/share/gnome-shell/extensions/places-menu@gnome-shell-extensions.gcampax.github.com/convenience.js
/usr/share/gnome-shell/extensions/places-menu@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/places-menu@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/places-menu@gnome-shell-extensions.gcampax.github.com/placeDisplay.js
/usr/share/gnome-shell/extensions/places-menu@gnome-shell-extensions.gcampax.github.com/stylesheet.css
/usr/share/gnome-shell/extensions/screenshot-window-sizer@gnome-shell-extensions.gcampax.github.com/convenience.js
/usr/share/gnome-shell/extensions/screenshot-window-sizer@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/screenshot-window-sizer@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/screenshot-window-sizer@gnome-shell-extensions.gcampax.github.com/stylesheet.css
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

