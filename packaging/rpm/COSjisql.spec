# $Id: COSjisql.spec,v 1.2 2012/11/10 17:51:14 jim Exp $
# (C) Nov 2010-Nov 2012 by Jim Klimov, JSC COS&HT
# RPM-build spec file for COSjisql package
# Copy it to the SPECS root of your RPM build area
# See Also: http://www.rpm.org/max-rpm/s1-rpm-build-creating-spec-file.html
### runs ok on buildhost as:
###   su - jim
###   cd rpm/BUILD
###   rpmbuild -bb COSjisql.spec
#
#
Summary: Java Interactive SQL client
Name: COSjisql
Version: 2.0.11
Release: 1
License: "(C) Xigole, http://www.xigole.com/software/jisql/jisql.jsp"
Group: Utilities
#Group: Applications/System
#Source: https://github.com/cos-ht/COSjisql
URL: https://github.com/cos-ht/COSjisql
Distribution: RHEL/CentOS 5 Linux
Vendor: Xigole, http://www.xigole.com/software/jisql/jisql.jsp; Packaged by JSC COS&HT (Center of Open Systems and High Technologies, MIPT, www.cos.ru)
Packager: Jim Klimov <jimklimov@cos.ru>
Prefix: /opt/COSas
BuildRoot: /tmp/rpmbuild-COSas

%description
Pure Java SQL clients with scripted wrappers.

# TODO: Make the new git repo layout usable for direct packaging in rules below
%prep
#set
WORKDIR="$RPM_BUILD_DIR/$RPM_PACKAGE_NAME-$RPM_PACKAGE_VERSION-$RPM_PACKAGE_RELEASE"
[ x"$RPM_BUILD_ROOT" != x ] && WORKDIR="$RPM_BUILD_ROOT"
rm -rf "$WORKDIR"
#mkdir -p "$WORKDIR"/opt/COSas/etc
#mkdir -p "$WORKDIR"/etc
#ln -s ../opt/COSas/etc "$WORKDIR"/etc/COSas
mkdir -p "$WORKDIR"/opt/COSas/bin && \
    tar c -C /home/jim/pkg/COSjisql*/bin --exclude CVS -f - . | \
    tar x -C "$WORKDIR"/opt/COSas/bin -f -
mkdir -p "$WORKDIR"/opt/COSas/lib && \
    tar c -C /home/jim/pkg/COSjisql*/lib --exclude CVS -f - \
	jopt-simple-4.3.jar javacsv-2.1.jar jisql-2.0.11.jar \
	mysql-connector-java-5.1.20-bin.jar \
    | tar x -C "$WORKDIR"/opt/COSas/lib -f -
mkdir -p "$WORKDIR"/opt/COSas/pkg && \
    tar c -C /home/jim/pkg/COSjisql* -f - COSjisql.spec | \
    tar x -C "$WORKDIR"/opt/COSas/pkg -f -

%files
%attr(755, bin, bin) %dir /opt/COSas
%attr(755, bin, bin) %dir /opt/COSas/bin
%attr(755, bin, bin) %dir /opt/COSas/lib
%attr(700, bin, bin) %dir /opt/COSas/pkg
%attr(-, bin, bin) /opt/COSas/pkg/COSjisql.spec
%attr(755, bin, bin) /opt/COSas/bin/mysqlj
%attr(644, bin, bin) /opt/COSas/lib/jopt-simple-4.3.jar
%attr(644, bin, bin) /opt/COSas/lib/javacsv-2.1.jar
%attr(644, bin, bin) /opt/COSas/lib/jisql-2.0.11.jar
%attr(644, bin, bin) /opt/COSas/lib/mysql-connector-java-5.1.20-bin.jar


%postun
#set -x
### For buggy old RPMs
[ x"$RPM_INSTALL_PREFIX" = x ] && RPM_INSTALL_PREFIX="/"
true

%post
#set -x
### For buggy old RPMs
[ x"$RPM_INSTALL_PREFIX" = x ] && RPM_INSTALL_PREFIX="/"
true
