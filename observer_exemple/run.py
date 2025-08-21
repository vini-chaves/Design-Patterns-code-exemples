from src import ConcreteSubject, ConcreteObserverA, ConcreteObserverB

if __name__ == "__main__":
    # The client code.
    # Should be similar to our Element Tree Controller
    subject = ConcreteSubject()
    print('Created the observer controller\n')

    #Should be similar to our Dehibitor of alarms
    observer_a = ConcreteObserverA()
    subject.attach(observer_a)
    #Should be similar to our Dehibitor of alarms
    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    #Should be similar to our Dehibitor of alarms
    print('\nDetach Observer a')
    subject.detach(observer_a)

    subject.some_business_logic()