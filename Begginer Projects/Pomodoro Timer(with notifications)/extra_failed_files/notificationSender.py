from win11toast import toast

buttons1 = [
    {'activationType': 'protocol', 'arguments': 'https://www.facebook.com/marketplace/', 'content': 'Open Marketplace'},
    {'activationType': 'protocol', 'arguments': 'file:///C:/', 'content': 'Continue Work'}
]

toast('Pomodoro Timer is Over!', 'Go rest by making some money!', buttons=buttons1)