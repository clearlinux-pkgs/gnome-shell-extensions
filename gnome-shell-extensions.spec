#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-shell-extensions
Version  : 40.1
Release  : 35
URL      : https://download.gnome.org/sources/gnome-shell-extensions/40/gnome-shell-extensions-40.1.tar.xz
Source0  : https://download.gnome.org/sources/gnome-shell-extensions/40/gnome-shell-extensions-40.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: gnome-shell-extensions-data = %{version}-%{release}
Requires: gnome-shell-extensions-license = %{version}-%{release}
Requires: gnome-shell-extensions-locales = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : gjs-dev
BuildRequires : mozjs78-dev
BuildRequires : pkgconfig(gio-2.0)

%description
# GNOME Shell Extensions
GNOME Shell Extensions is a collection of extensions providing additional
and optional functionality to GNOME Shell.

%package data
Summary: data components for the gnome-shell-extensions package.
Group: Data

%description data
data components for the gnome-shell-extensions package.


%package license
Summary: license components for the gnome-shell-extensions package.
Group: Default

%description license
license components for the gnome-shell-extensions package.


%package locales
Summary: locales components for the gnome-shell-extensions package.
Group: Default

%description locales
locales components for the gnome-shell-extensions package.


%prep
%setup -q -n gnome-shell-extensions-40.1
cd %{_builddir}/gnome-shell-extensions-40.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1622762505
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dextension_set='all'  builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-shell-extensions
cp %{_builddir}/gnome-shell-extensions-40.1/COPYING %{buildroot}/usr/share/package-licenses/gnome-shell-extensions/a49ccf4ee26e90b0baa0cdd4cf2ae9bb3b0ff67d
cp %{_builddir}/gnome-shell-extensions-40.1/data/gnome-shell-sass/COPYING %{buildroot}/usr/share/package-licenses/gnome-shell-extensions/a49ccf4ee26e90b0baa0cdd4cf2ae9bb3b0ff67d
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-shell-extensions

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/glib-2.0/schemas/org.gnome.shell.extensions.auto-move-windows.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.shell.extensions.native-window-placement.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.shell.extensions.screenshot-window-sizer.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.shell.extensions.user-theme.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.shell.extensions.window-list.gschema.xml
/usr/share/gnome-shell/extensions/apps-menu@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/apps-menu@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/apps-menu@gnome-shell-extensions.gcampax.github.com/stylesheet.css
/usr/share/gnome-shell/extensions/auto-move-windows@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/auto-move-windows@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/auto-move-windows@gnome-shell-extensions.gcampax.github.com/prefs.js
/usr/share/gnome-shell/extensions/auto-move-windows@gnome-shell-extensions.gcampax.github.com/stylesheet.css
/usr/share/gnome-shell/extensions/drive-menu@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/drive-menu@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/drive-menu@gnome-shell-extensions.gcampax.github.com/stylesheet.css
/usr/share/gnome-shell/extensions/launch-new-instance@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/launch-new-instance@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/launch-new-instance@gnome-shell-extensions.gcampax.github.com/stylesheet.css
/usr/share/gnome-shell/extensions/native-window-placement@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/native-window-placement@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/native-window-placement@gnome-shell-extensions.gcampax.github.com/stylesheet.css
/usr/share/gnome-shell/extensions/places-menu@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/places-menu@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/places-menu@gnome-shell-extensions.gcampax.github.com/placeDisplay.js
/usr/share/gnome-shell/extensions/places-menu@gnome-shell-extensions.gcampax.github.com/stylesheet.css
/usr/share/gnome-shell/extensions/screenshot-window-sizer@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/screenshot-window-sizer@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/screenshot-window-sizer@gnome-shell-extensions.gcampax.github.com/stylesheet.css
/usr/share/gnome-shell/extensions/user-theme@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/user-theme@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/user-theme@gnome-shell-extensions.gcampax.github.com/prefs.js
/usr/share/gnome-shell/extensions/user-theme@gnome-shell-extensions.gcampax.github.com/stylesheet.css
/usr/share/gnome-shell/extensions/user-theme@gnome-shell-extensions.gcampax.github.com/util.js
/usr/share/gnome-shell/extensions/window-list@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/window-list@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/window-list@gnome-shell-extensions.gcampax.github.com/prefs.js
/usr/share/gnome-shell/extensions/window-list@gnome-shell-extensions.gcampax.github.com/stylesheet.css
/usr/share/gnome-shell/extensions/window-list@gnome-shell-extensions.gcampax.github.com/windowPicker.js
/usr/share/gnome-shell/extensions/window-list@gnome-shell-extensions.gcampax.github.com/workspaceIndicator.js
/usr/share/gnome-shell/extensions/windowsNavigator@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/windowsNavigator@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/windowsNavigator@gnome-shell-extensions.gcampax.github.com/stylesheet.css
/usr/share/gnome-shell/extensions/workspace-indicator@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/workspace-indicator@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/workspace-indicator@gnome-shell-extensions.gcampax.github.com/prefs.js
/usr/share/gnome-shell/extensions/workspace-indicator@gnome-shell-extensions.gcampax.github.com/stylesheet.css

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-shell-extensions/a49ccf4ee26e90b0baa0cdd4cf2ae9bb3b0ff67d

%files locales -f gnome-shell-extensions.lang
%defattr(-,root,root,-)

