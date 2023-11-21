from receptor import DelayedReceptor


def test_initial_values_in_receptor():
    # given
    expected_signal = 0.2

    # when
    receptor = DelayedReceptor(threshold=5, delay=4, initial_value=4)

    # then
    assert receptor.read_signal() == expected_signal
    assert receptor.read_signal() == expected_signal
    assert receptor.read_signal() == expected_signal
    assert receptor.read_signal() == expected_signal


def test_read_signal_forgets_values():
    # given
    receptor = DelayedReceptor(threshold=5, delay=3, initial_value=1)

    # when
    receptor.read_signal()
    receptor.update(2)

    # then
    assert receptor.read_signal() == 0.8
    assert receptor.read_signal() == 0.8
    assert receptor.read_signal() == 0.6


def test_receptor_memory_is_fifo():
    # given
    receptor = DelayedReceptor(threshold=5, delay=3, initial_value=1)

    # when
    receptor.read_signal()
    receptor.read_signal()
    receptor.read_signal()
    receptor.update(5)
    receptor.update(4)
    receptor.update(1)

    # then
    assert receptor.read_signal() == 0
    assert receptor.read_signal() == 0.2
    assert receptor.read_signal() == 0.8


def test_signal_is_never_negative():
    # given
    receptor = DelayedReceptor(threshold=5, delay=1, initial_value=6)

    # when / then
    assert receptor.read_signal() == 0
