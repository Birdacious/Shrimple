# This fork

My version of Shrimple, for my gamepad-based system. This version focusees less on orthospelling speed, and more on the ability to type numbers and symbols (on the RHS) which is useful for programming — for vim motions, and for faster two-handed fingerspelling of short variable names. Not meant to be the primary mode for programming, a specialized dictionary for each programming language is better. This is just a supplement.
Intended to be SOLO_DICT'd (using plover-dict-commands) alongside the override dictionary just above it.

Below is the original Shrimple README:

# Shrimple
Shrimple: a Python dictionary you can use to run your orthospelling theory

## What is orthospelling?
After defining your chords, Shrimple will make any combination valid

Even if you don't have "thou hath thee" in your dictionaries, you can Shrimple them in a single stroke, because the chords that make up the stroke are defined already.

```
Example Shrimple chords:
T → t
H → h
AOE → ee
O → o
*T → th
U → u
```
```
Example Shrimple ouputs
🦐THOU → thou
🦐HA\*T → hath
🦐THAOE → thee
```

But of course most chords are exactly what you expect, so you should be able to use Shrimple already!
```
🦐TKOG → dog
🦐STOEUPB → stoin
🦐PHAEUPB → mane (AEU is 'a_e' not 'ai')
🦐PHAOEUT → mite
🦐STEPB/OG/RAP/H*D → stenography (I use *D → y)
```



This is about as Shromplicated as it gets: (If you chose to one-stroke it of course)

`🦐#SKHR*EUFRPLD → Shrimple`
Using the logic:
```
# → capitalisation (Lapwing theory)
SKHR → shr (Josiah theory)
FRPL → mple (Plover theory)
*D is for {^y} (Josiah theory)
```


## What's the 🦐?

It's whatever you use to enter Shrimple mode, by default it's the stroke "SHREUFRPL", but I use a dedicated + key to save me a stroke

## "I'm stuck in Shrimple"
Use any punctuation to exit, if I forgot to include whatever stroke you use for punctuation, you can add it to the exit strokes
Or if you use a dedicated key, you can make Shrimple always exit after just a single stroke
