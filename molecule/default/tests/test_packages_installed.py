import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_transmission_package(Package):
    p = Package('transmission-daemon')
    assert p.is_installed


def test_transmissoion_running_and_enabled(Service):
    service = Service("transmission-daemon.service")
    assert service.is_running
    assert service.is_enabled
