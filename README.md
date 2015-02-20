# orwelliangenerator
script that uses markov chains to imitate the writing of the great George Orwell.

usage
=====

```
tester = Markov('file.txt')
print tester.makeChain(20)
```

the parameter for ```makeChain()``` is more like a suggestion. it will go until it feels like it generally. 

also, sometimes it will hit recursion limit and scream and die.
