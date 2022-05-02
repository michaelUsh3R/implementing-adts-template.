from QueueArray import QueueArray

def test_is_empty():
    s = QueueArray()
    assert s.is_empty()

def test_enq_empty():
    s = QueueArray()
    s.enq(5)
    assert not s.is_empty()

def test_enq_tail():
    s = QueueArray()
    s.enq(5)
    assert s.get_tail() == 5

def test_enq_front():
    s = QueueArray()
    s.enq(5)
    assert s.get_front() == 5

def test_deq():
    s = QueueArray()
    s.enq(5)
    assert s.deq() == 5

def test_deq_empty():
    s = QueueArray()
    s.enq(5)
    s.deq()
    assert s.is_empty()

def test_enq_many_empty():
    s = QueueArray()
    s.enq(15)
    s.enq(16)
    s.enq(17)
    assert not s.is_empty()

def test_enq_many_tail():
    s = QueueArray()
    s.enq(15)
    s.enq(16)
    s.enq(17)
    assert s.get_tail() == 17

def test_enq_many_front():
    s = QueueArray()
    s.enq(15)
    s.enq(16)
    s.enq(17)
    assert s.get_front() == 15

def test_enq_many_deq():
    s = QueueArray()
    s.enq(15)
    s.enq(16)
    s.enq(17)
    assert s.deq() == 15

def test_deq_empty():
    s = QueueArray()
    assert s.deq() is None

def test_clear_empty():
    s = QueueArray()
    s.enq(5)
    s.clear()
    assert s.is_empty()

def test_enq_deq_many():
    s = QueueArray()
    le = []
    la = []
    for i in range(20,201,10):
        s.enq(i)
        le.append(i)
    while not s.is_empty():
        la.append(s.deq())
    assert le == la