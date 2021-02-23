This is where Sleigh stores rules. They are stored in folders as "groups".
Each folder name can **either** be a Machine ID or a Machine Owner, so don't
name your machine IDs the same as your machine owners!

In addition, rules are combined based on what your machine info has, so if your
machine had BOTH a matching ID and owner, it would receive three sets of rules,
with the third being the *global* ruleset.

Example as I am struggling to explain this with words:
  Rule Hierarchy:

  ABCD-EFGH-IJKL/         (machine id)
    some_rule_1.json
    some_rule_2.json

  andre4ik3/              (machine owner)
    some_rule_3.json
    some_rule_4.json

  global/                 (global ruleset)
    default_rule_1.json
    default_rule_2.json


  Machines:

    Machine A:
      ID: ABCD-EFGH-IJKL
      Owner: None
  
      Would Receive Rules from Folders:
        ABCD-EFGH-IJKL/**
        global/**
  
    Machine B:
      ID: MNOP-QRST-UVWX
      Owner: andre4ik3
  
      Would Receive Rules from Folders:
        andre4ik3/**
        global/**

    Machine C:
      ID: ABCD-EFGH-IJKL
      Owner: andre4ik3

      Would Receive Rules from Folders:
        ABCD-EFGH-IJKL/**
        andre4ik3/**
        global/**

That example should be enough for you to grasp how the rule hierarchy is built.
Read the wiki for more info.
And, yes, you can have folders with rules inside of the machine group folders.
