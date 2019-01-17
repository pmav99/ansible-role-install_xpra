import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_xpra_is_installed(host):
    xpra = host.package("xpra")
    assert xpra.is_installed
    assert xpra.version.startswith("2.")
