Name:		texlive-texworks
Version:	54074
Release:	2
Summary:	friendly cross-platform front end
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/texworks
License:	
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texworks.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texworks.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
See http://tug.org/texworks for information and downloads. TeX
Live includes executables and support files only for Windows.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%doc %{_texmfdistdir}/texmf-dist/doc/texworks

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
