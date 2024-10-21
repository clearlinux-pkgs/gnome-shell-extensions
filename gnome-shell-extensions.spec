#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v20
# autospec commit: f35655a
#
Name     : gnome-shell-extensions
Version  : 47.1
Release  : 61
URL      : https://download.gnome.org/sources/gnome-shell-extensions/47/gnome-shell-extensions-47.1.tar.xz
Source0  : https://download.gnome.org/sources/gnome-shell-extensions/47/gnome-shell-extensions-47.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0 LGPL-2.0 MIT
Requires: gnome-shell-extensions-data = %{version}-%{release}
Requires: gnome-shell-extensions-license = %{version}-%{release}
Requires: gnome-shell-extensions-locales = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : gjs-dev
BuildRequires : pkgconfig(gio-2.0)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n gnome-shell-extensions-47.1
cd %{_builddir}/gnome-shell-extensions-47.1
pushd ..
cp -a gnome-shell-extensions-47.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1729530258
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dextension_set='all'  builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dextension_set='all'  builddiravx2
ninja -v -C builddiravx2

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-shell-extensions
cp %{_builddir}/gnome-shell-extensions-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gnome-shell-extensions/a49ccf4ee26e90b0baa0cdd4cf2ae9bb3b0ff67d || :
cp %{_builddir}/gnome-shell-extensions-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/gnome-shell-extensions/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/gnome-shell-extensions-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/gnome-shell-extensions/3cb34cfc72e87654683f2894299adf912d14b284 || :
cp %{_builddir}/gnome-shell-extensions-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/gnome-shell-extensions/5c6c38fa1b6ac7c66252c83d1203e997ae3d1c98 || :
cp %{_builddir}/gnome-shell-extensions-%{version}/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/gnome-shell-extensions/adadb67a9875aeeac285309f1eab6e47d9ee08a7 || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-shell-extensions
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/glib-2.0/schemas/org.gnome.shell.extensions.apps-menu.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.shell.extensions.auto-move-windows.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.shell.extensions.native-window-placement.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.shell.extensions.screenshot-window-sizer.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.shell.extensions.system-monitor.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.shell.extensions.user-theme.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.shell.extensions.window-list.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.shell.extensions.workspace-indicator.gschema.xml
/usr/share/gnome-shell/extensions/apps-menu@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/apps-menu@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/apps-menu@gnome-shell-extensions.gcampax.github.com/stylesheet.css
/usr/share/gnome-shell/extensions/auto-move-windows@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/auto-move-windows@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/auto-move-windows@gnome-shell-extensions.gcampax.github.com/prefs.js
/usr/share/gnome-shell/extensions/drive-menu@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/drive-menu@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/drive-menu@gnome-shell-extensions.gcampax.github.com/stylesheet.css
/usr/share/gnome-shell/extensions/launch-new-instance@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/launch-new-instance@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/light-style@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/light-style@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/native-window-placement@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/native-window-placement@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/places-menu@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/places-menu@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/places-menu@gnome-shell-extensions.gcampax.github.com/placeDisplay.js
/usr/share/gnome-shell/extensions/places-menu@gnome-shell-extensions.gcampax.github.com/stylesheet.css
/usr/share/gnome-shell/extensions/screenshot-window-sizer@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/screenshot-window-sizer@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/screenshot-window-sizer@gnome-shell-extensions.gcampax.github.com/stylesheet.css
/usr/share/gnome-shell/extensions/status-icons@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/status-icons@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/system-monitor@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/system-monitor@gnome-shell-extensions.gcampax.github.com/icons/download-symbolic.svg
/usr/share/gnome-shell/extensions/system-monitor@gnome-shell-extensions.gcampax.github.com/icons/download-symbolic.svg.license
/usr/share/gnome-shell/extensions/system-monitor@gnome-shell-extensions.gcampax.github.com/icons/memory-symbolic.svg
/usr/share/gnome-shell/extensions/system-monitor@gnome-shell-extensions.gcampax.github.com/icons/memory-symbolic.svg.license
/usr/share/gnome-shell/extensions/system-monitor@gnome-shell-extensions.gcampax.github.com/icons/processor-symbolic.svg
/usr/share/gnome-shell/extensions/system-monitor@gnome-shell-extensions.gcampax.github.com/icons/processor-symbolic.svg.license
/usr/share/gnome-shell/extensions/system-monitor@gnome-shell-extensions.gcampax.github.com/icons/swap-symbolic.svg
/usr/share/gnome-shell/extensions/system-monitor@gnome-shell-extensions.gcampax.github.com/icons/swap-symbolic.svg.license
/usr/share/gnome-shell/extensions/system-monitor@gnome-shell-extensions.gcampax.github.com/icons/upload-symbolic.svg
/usr/share/gnome-shell/extensions/system-monitor@gnome-shell-extensions.gcampax.github.com/icons/upload-symbolic.svg.license
/usr/share/gnome-shell/extensions/system-monitor@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/system-monitor@gnome-shell-extensions.gcampax.github.com/stylesheet.css
/usr/share/gnome-shell/extensions/user-theme@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/user-theme@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/user-theme@gnome-shell-extensions.gcampax.github.com/prefs.js
/usr/share/gnome-shell/extensions/user-theme@gnome-shell-extensions.gcampax.github.com/util.js
/usr/share/gnome-shell/extensions/window-list@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/window-list@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/window-list@gnome-shell-extensions.gcampax.github.com/prefs.js
/usr/share/gnome-shell/extensions/window-list@gnome-shell-extensions.gcampax.github.com/stylesheet-dark.css
/usr/share/gnome-shell/extensions/window-list@gnome-shell-extensions.gcampax.github.com/stylesheet-light.css
/usr/share/gnome-shell/extensions/window-list@gnome-shell-extensions.gcampax.github.com/stylesheet-workspace-switcher-dark.css
/usr/share/gnome-shell/extensions/window-list@gnome-shell-extensions.gcampax.github.com/stylesheet-workspace-switcher-light.css
/usr/share/gnome-shell/extensions/window-list@gnome-shell-extensions.gcampax.github.com/workspaceIndicator.js
/usr/share/gnome-shell/extensions/windowsNavigator@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/windowsNavigator@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/windowsNavigator@gnome-shell-extensions.gcampax.github.com/stylesheet.css
/usr/share/gnome-shell/extensions/workspace-indicator@gnome-shell-extensions.gcampax.github.com/extension.js
/usr/share/gnome-shell/extensions/workspace-indicator@gnome-shell-extensions.gcampax.github.com/metadata.json
/usr/share/gnome-shell/extensions/workspace-indicator@gnome-shell-extensions.gcampax.github.com/prefs.js
/usr/share/gnome-shell/extensions/workspace-indicator@gnome-shell-extensions.gcampax.github.com/stylesheet-dark.css
/usr/share/gnome-shell/extensions/workspace-indicator@gnome-shell-extensions.gcampax.github.com/stylesheet-light.css
/usr/share/gnome-shell/extensions/workspace-indicator@gnome-shell-extensions.gcampax.github.com/workspaceIndicator.js

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-shell-extensions/3cb34cfc72e87654683f2894299adf912d14b284
/usr/share/package-licenses/gnome-shell-extensions/5c6c38fa1b6ac7c66252c83d1203e997ae3d1c98
/usr/share/package-licenses/gnome-shell-extensions/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/gnome-shell-extensions/a49ccf4ee26e90b0baa0cdd4cf2ae9bb3b0ff67d
/usr/share/package-licenses/gnome-shell-extensions/adadb67a9875aeeac285309f1eab6e47d9ee08a7

%files locales -f gnome-shell-extensions.lang
%defattr(-,root,root,-)

