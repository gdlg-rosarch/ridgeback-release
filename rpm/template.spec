Name:           ros-indigo-ridgeback-control
Version:        0.1.0
Release:        0%{?dist}
Summary:        ROS ridgeback_control package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/ridgeback_control
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-controller-interface
Requires:       ros-indigo-controller-manager
Requires:       ros-indigo-interactive-marker-twist-server
Requires:       ros-indigo-joint-state-controller
Requires:       ros-indigo-joy
Requires:       ros-indigo-nav-msgs
Requires:       ros-indigo-realtime-tools
Requires:       ros-indigo-robot-localization
Requires:       ros-indigo-teleop-twist-joy
Requires:       ros-indigo-tf
Requires:       ros-indigo-topic-tools
Requires:       ros-indigo-urdf
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-controller-interface
BuildRequires:  ros-indigo-controller-manager
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-realtime-tools
BuildRequires:  ros-indigo-roslaunch
BuildRequires:  ros-indigo-tf
BuildRequires:  ros-indigo-urdf

%description
Controllers for Ridgeback

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
* Thu Nov 19 2015 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.1.0-0
- Autogenerated by Bloom

