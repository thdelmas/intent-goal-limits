# Spec: quiet hours in the open-plan office

cost_class: irreversible

## Intent

People can do focused work in the office without leaving it.

## Goal

Between 10:00 and 12:00 nobody in the room is interrupted by speech or calls. Counted by a weekly self-report; fails if more than one person reports an interruption in the window.

## Limits

| Cost | Bearer (seat) | Seat | Balance as the bearer sees it | Fires when |
| --- | --- | --- | --- | --- |
| Support staff cannot take incoming calls for two hours | the support team | filled | Acceptable if calls roll to voicemail with a callback promise; not acceptable if the queue counts against them | A missed call in the window is counted against anyone's queue |
| A safety alarm or a colleague asking for help is treated as noise | anyone in the room during an emergency | empty | | Anyone is shushed while asking for help |
| People who think aloud lose their working mode | the two engineers who pair by talking | filled | Not acceptable as written; they asked for one bookable talking desk outside the room | The rule goes on the wall before the desk exists |
| Fire-safety rules on blocking doors or muting alarms | everyone the building code protects; pre-existing seat, the code is its answer | filled | Building code, read: alarms are never in scope of "noise" | Any proposed measure touches an alarm or an exit |

## Open

The pairing engineers' answer and the goal disagree: the goal says nobody speaks, their seat says one desk does. Both stand; the limit stays open until the desk exists or the goal is revised. The emergency seat is empty and irreversible, so this spec cannot close and no rule goes on the wall yet.
