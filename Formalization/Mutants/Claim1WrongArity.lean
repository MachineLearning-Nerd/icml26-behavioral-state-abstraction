import Formalization.Core

open BehavioralSemantics

def binaryBundle : Bundle Nat 2 Bool :=
  fun tuple => tuple 0 = tuple 1

def unaryTuple : Tuple Nat 1 :=
  fun _ => 0

example : Bool := binaryBundle unaryTuple
