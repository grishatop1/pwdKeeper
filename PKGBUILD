# Maintainer: Felix Yan <felixonmars@archlinux.org>

pkgname=pwdkeeper
pkgver=1.0
pkgdesc="A very simple and secure tool for managing passwords (qt5)"
arch=('any')
url="https://github.com/grishatop1/pwdKeeper"
license=('MIT')
depends=('python-pyqt5' 'python-cryptography' 'python-zxcvbn')
makedepends=('python-pip')
source=("https://github.com/nvbn/thefuck/archive/$pkgver/$pkgname-$pkgver.tar.gz")
sha512sums=('961b9b6dc374cc0b854698455f688cf110adb21cfebd4cb645eb5f1ce11c14de6699bb4d40de86a5f9461273cbfc2eea318a9d437f803dc578dd431966cf26c1')

build() {
  cd pwdk-$pkgver
  python setup.py build
}

package() {
  cd pwdk-$pkgver
  python setup.py install -O1 --prefix=/usr --root="$pkgdir"
}
