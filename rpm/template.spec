Name:           ros-indigo-ridgeback-navigation
Version:        0.1.11
Release:        0%{?dist}
Summary:        ROS ridgeback_navigation package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-amcl
Requires:       ros-indigo-gmapping
Requires:       ros-indigo-map-server
Requires:       ros-indigo-move-base
Requires:       ros-indigo-urdf
Requires:       ros-indigo-xacro
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-roslaunch

%description
Launch files and code for autonomous navigation of the Ridgeback

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Apr 12 2018 Tony Baltovski <tbaltovski@clearpathrobotics.com> - 0.1.11-0
- Autogenerated by Bloom

* Mon Jun 26 2017 Tony Baltovski <tbaltovski@clearpathrobotics.com> - 0.1.10-0
- Autogenerated by Bloom

* Mon Apr 17 2017 Tony Baltovski <tbaltovski@clearpathrobotics.com> - 0.1.9-0
- Autogenerated by Bloom

* Fri Sep 30 2016 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.1.8-0
- Autogenerated by Bloom

* Mon Jul 18 2016 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.1.7-0
- Autogenerated by Bloom

* Wed May 25 2016 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.1.6-0
- Autogenerated by Bloom

* Fri Apr 22 2016 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.1.5-0
- Autogenerated by Bloom

* Mon Apr 18 2016 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.1.4-0
- Autogenerated by Bloom

* Thu Nov 19 2015 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.1.0-0
- Autogenerated by Bloom

