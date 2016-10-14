Name:		mylog
Version:	1.0
Release:    1
License:	GPL
Source0:	mylog
Source1:	mylog.conf
Source2:	mylog_logrotate
Source3:	mylog_cron
Source4:	mylog.service
Summary:	aaa
Requires:	rsyslog, logrotate, systemd

%description
oneshot-юнит, который при старте системы, а также каждые 20 минут пишет в сислог отчет о занятом месте на диске, конфигурирует отдельный лог /var/log/mylog.log для этого отчета, а также ежедневную ротацию данного лога со сжатием

%install
install -D -m 755 %{SOURCE0} $RPM_BUILD_ROOT/usr/bin/mylog
install -D -m 644 %{SOURCE1} $RPM_BUILD_ROOT/etc/rsyslog.d/mylog.conf
install -D -m 644 %{SOURCE2} $RPM_BUILD_ROOT/etc/logrotate.d/mylog_logrotate
install -D -m 644 %{SOURCE3} $RPM_BUILD_ROOT/etc/cron.d/mylog_cron
install -D -m 644 %{SOURCE4} $RPM_BUILD_ROOT/etc/systemd/system/mylog.service

%post
systemctl restart rsyslog
systemctl enable mylog

%preun
systemctl disable mylog

%postun
systemctl restart rsyslog

%files
%defattr(-, root, root, -)
/usr/bin/mylog
/etc/rsyslog.d/mylog.conf
/etc/logrotate.d/mylog_logrotate
/etc/cron.d/mylog_cron
/etc/systemd/system/mylog.service

