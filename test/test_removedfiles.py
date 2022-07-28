#
# Copyright © 2020 Red Hat, Inc.
# Author(s): David Cantrell <dcantrell@redhat.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import os
import rpmfluff

from baseclass import TestCompareRPMs, TestCompareKoji

datadir = os.environ["RPMINSPECT_TEST_DATA_PATH"] + "/compression/"


# gzip file does not change between builds despite having different
# compression ratios
class GzipFileNoRemovedRPMs(TestCompareRPMs):
    def setUp(self):
        super().setUp()

        # two files with the same data, but compressed differently
        with open(datadir + "test1-low.gz", "rb") as f:
            before_src = f.read()

        with open(datadir + "test1-low.gz", "rb") as f:
            after_src = f.read()

        # create the test packages
        self.before_rpm.add_installed_file(
            "/usr/etc/firmware.gz", rpmfluff.SourceFile("firmware.gz", before_src)
        )
        self.after_rpm.add_installed_file(
            "/usr/etc/firmware.gz", rpmfluff.SourceFile("firmware.gz", after_src)
        )

        self.inspection = "removedfiles"
        self.result = "OK"
        self.waiver_auth = "Not Waivable"


class GzipFileNoRemovedKoji(TestCompareKoji):
    def setUp(self):
        super().setUp()

        # two files with the same data, but compressed differently
        with open(datadir + "test1-low.gz", "rb") as f:
            before_src = f.read()

        with open(datadir + "test1-low.gz", "rb") as f:
            after_src = f.read()

        # create the test packages
        self.before_rpm.add_installed_file(
            "/usr/etc/firmware.gz", rpmfluff.SourceFile("firmware.gz", before_src)
        )
        self.after_rpm.add_installed_file(
            "/usr/etc/firmware.gz", rpmfluff.SourceFile("firmware.gz", after_src)
        )

        self.inspection = "removedfiles"
        self.result = "OK"
        self.waiver_auth = "Not Waivable"


# gzip file changes between builds and has different compression ratios
class GzipFileRemovedRPMs(TestCompareRPMs):
    def setUp(self):
        super().setUp()

        # two files with the same data, but compressed differently
        with open(datadir + "test1-low.gz", "rb") as f:
            before_src = f.read()

        # create the test package
        self.before_rpm.add_installed_file(
            "/usr/etc/firmware.gz", rpmfluff.SourceFile("firmware.gz", before_src)
        )

        self.inspection = "removedfiles"
        self.result = "OK"
        self.waiver_auth = "Not Waivable"


class GzipFileRemovedKoji(TestCompareKoji):
    def setUp(self):
        super().setUp()

        # two files with the same data, but compressed differently
        with open(datadir + "test1-low.gz", "rb") as f:
            before_src = f.read()

        # create the test package
        self.before_rpm.add_installed_file(
            "/usr/etc/firmware.gz", rpmfluff.SourceFile("firmware.gz", before_src)
        )

        self.inspection = "removedfiles"
        self.result = "OK"
        self.waiver_auth = "Not Waivable"


# bzip2 file does not change between builds despite having different
# compression ratios
class Bzip2FileNoRemovedRPMs(TestCompareRPMs):
    def setUp(self):
        super().setUp()

        # two files with the same data, but compressed differently
        with open(datadir + "test1-low.bz2", "rb") as f:
            before_src = f.read()

        with open(datadir + "test1-low.bz2", "rb") as f:
            after_src = f.read()

        # create the test packages
        self.before_rpm.add_installed_file(
            "/usr/etc/firmware.bz2", rpmfluff.SourceFile("firmware.bz2", before_src)
        )
        self.after_rpm.add_installed_file(
            "/usr/etc/firmware.bz2", rpmfluff.SourceFile("firmware.bz2", after_src)
        )

        self.inspection = "removedfiles"
        self.result = "OK"
        self.waiver_auth = "Not Waivable"


class Bzip2FileNoRemovedKoji(TestCompareKoji):
    def setUp(self):
        super().setUp()

        # two files with the same data, but compressed differently
        with open(datadir + "test1-low.bz2", "rb") as f:
            before_src = f.read()

        with open(datadir + "test1-low.bz2", "rb") as f:
            after_src = f.read()

        # create the test packages
        self.before_rpm.add_installed_file(
            "/usr/etc/firmware.bz2", rpmfluff.SourceFile("firmware.bz2", before_src)
        )
        self.after_rpm.add_installed_file(
            "/usr/etc/firmware.bz2", rpmfluff.SourceFile("firmware.bz2", after_src)
        )

        self.inspection = "removedfiles"
        self.result = "OK"
        self.waiver_auth = "Not Waivable"


# bzip2 file changes between builds and has different compression ratios
class Bzip2FileRemovedRPMs(TestCompareRPMs):
    def setUp(self):
        super().setUp()

        # two files with the same data, but compressed differently
        with open(datadir + "test1-low.bz2", "rb") as f:
            before_src = f.read()

        # create the test package
        self.before_rpm.add_installed_file(
            "/usr/etc/firmware.bz2", rpmfluff.SourceFile("firmware.bz2", before_src)
        )

        self.inspection = "removedfiles"
        self.result = "OK"
        self.waiver_auth = "Not Waivable"


class Bzip2FileRemovedKoji(TestCompareKoji):
    def setUp(self):
        super().setUp()

        # two files with the same data, but compressed differently
        with open(datadir + "test1-low.bz2", "rb") as f:
            before_src = f.read()

        # create the test package
        self.before_rpm.add_installed_file(
            "/usr/etc/firmware.bz2", rpmfluff.SourceFile("firmware.bz2", before_src)
        )

        self.inspection = "removedfiles"
        self.result = "OK"
        self.waiver_auth = "Not Waivable"


# xz file does not change between builds despite having different
# compression ratios
class XzFileNoRemovedRPMs(TestCompareRPMs):
    def setUp(self):
        super().setUp()

        # two files with the same data, but compressed differently
        with open(datadir + "test2-low.xz", "rb") as f:
            before_src = f.read()

        with open(datadir + "test2-low.xz", "rb") as f:
            after_src = f.read()

        # create the test packages
        self.before_rpm.add_installed_file(
            "/usr/etc/firmware.xz", rpmfluff.SourceFile("firmware.xz", before_src)
        )
        self.after_rpm.add_installed_file(
            "/usr/etc/firmware.xz", rpmfluff.SourceFile("firmware.xz", after_src)
        )

        self.inspection = "removedfiles"
        self.result = "OK"
        self.waiver_auth = "Not Waivable"


class XzFileNoRemovedKoji(TestCompareKoji):
    def setUp(self):
        super().setUp()

        # two files with the same data, but compressed differently
        with open(datadir + "test1-low.xz", "rb") as f:
            before_src = f.read()

        with open(datadir + "test1-low.xz", "rb") as f:
            after_src = f.read()

        # create the test packages
        self.before_rpm.add_installed_file(
            "/usr/etc/firmware.xz", rpmfluff.SourceFile("firmware.xz", before_src)
        )
        self.after_rpm.add_installed_file(
            "/usr/etc/firmware.xz", rpmfluff.SourceFile("firmware.xz", after_src)
        )

        self.inspection = "removedfiles"
        self.result = "OK"
        self.waiver_auth = "Not Waivable"


# xz file changes between builds and has different compression ratios
class XzFileRemovedRPMs(TestCompareRPMs):
    def setUp(self):
        super().setUp()

        # two files with the same data, but compressed differently
        with open(datadir + "test1-low.xz", "rb") as f:
            before_src = f.read()

        # create the test package
        self.before_rpm.add_installed_file(
            "/usr/etc/firmware.xz", rpmfluff.SourceFile("firmware.xz", before_src)
        )

        self.inspection = "removedfiles"
        self.result = "OK"
        self.waiver_auth = "Not Waivable"


class XzFileRemovedKoji(TestCompareKoji):
    def setUp(self):
        super().setUp()

        # two files with the same data, but compressed differently
        with open(datadir + "test1-low.xz", "rb") as f:
            before_src = f.read()

        # create the test package
        self.before_rpm.add_installed_file(
            "/usr/etc/firmware.xz", rpmfluff.SourceFile("firmware.xz", before_src)
        )

        self.inspection = "removedfiles"
        self.result = "OK"
        self.waiver_auth = "Not Waivable"