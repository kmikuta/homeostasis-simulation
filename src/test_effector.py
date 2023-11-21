from effector import Effector


def test_effector_performs_production():
    # given
    effector = Effector(molecular_activity=4)

    # when / then
    assert effector.perform_production(signal=1) == 4
    assert effector.perform_production(signal=0.5) == 2
    assert effector.perform_production(signal=0.01) == 0.04
