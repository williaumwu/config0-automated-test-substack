"""
# Copyright (C) 2025 Gary Leong <gary@config0.com>
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
# vpc_substack — small standalone sub-stack fixture (config0-automated-test-substack).
# Pulled in by run_test_stack via add_substack. Pulls the group0 script so a
# CONTENT change here rolls up to the parent stack through the dependency resolver.
"""

def run(stackargs):

    # instantiate authoring stack
    stack = newStack(stackargs)

    # optional variables
    stack.parse.add_optional(key="vpc_cidr",
                             types="str",
                             default="10.0.0.0/16")

    # depends on the group0 leaf script (so substack content rolls up to parent)
    stack.add_script("williaumwu:::config0-automated-test-group0::resource_wrapper.sh")

    # initialize
    stack.init_variables()

    return stack.get_results()
