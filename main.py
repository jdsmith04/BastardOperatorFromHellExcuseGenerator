"""
Bastard Operator From Hell and Bastard D.I.Y. Excuse board are property of Simon Travaglia
and the original excuse board can be found here at this site for your enjoyment.
http://bofh.bjash.com/ExcuseBoard.html
"""
import random


def main():
    # 4 list of words to choose from for technical excuse
    # 4th list is optional
    first_word_list = ['Temporary', 'Intermittent', 'Partial', 'Redundant', 'Total', 'Multiplexed', 'Inherent',
                       'Duplicated', 'Dual-Homed', 'Synchronous', 'Bidirectional', 'Serial', 'Asynchronous',
                       'Multiple', 'Replicated', 'Non-Replicated', 'Unregistered', 'Non-Specific', 'Generic',
                       'Migrated', 'Localised', 'Resignalled', 'Dereferenced', 'Nullified', 'Aborted', 'Serious',
                       'Minor', 'Major', 'Extraneous', 'Illegal', 'Insufficient', 'Viral', 'Unsupported', 'Outmoded',
                       'Legacy', 'Permanent', 'Invalid', 'Deprecated', 'Virtual', 'Unreportable', 'Undetermined',
                       'Undiagnosable', 'Unfiltered', 'Static', 'Dynamic', 'Delayed', 'Immediate', 'Nonfatal',
                       'Fatal', 'Non-Valid', 'Unvalidated', 'Non-Static', 'Unreplicatable', 'Non-Serious']

    second_word_list = ['Array', 'Systems', 'Hardware', 'Software', 'Firmware', 'Backplane', 'Logic-Subsystem',
                        'Integrity', 'Subsystem', 'Memory', 'Comms', 'Integrity', 'Checksum', 'Protocol', 'Parity',
                        'Bus', 'Timing', 'Synchronisation', 'Topology', 'Transmission', 'Reception', 'Stack',
                        'Framing', 'Code', 'Programming', 'Peripheral', 'Environmental', 'Loading', 'Operation',
                        'Parameter', 'Syntax', 'Initialisation', 'Execution', 'Resource', 'Encryption', 'Decryption',
                        'File', 'Precondition', 'Authentication', 'Paging', 'Swapfile', 'Service', 'Gateway',
                        'Request', 'Proxy', 'Media', 'Registry', 'Configuration', 'Metadata', 'Streaming',
                        'Retrieval', 'Installation', 'Library', 'Handler']

    third_word_list = ['Interruption', 'Destabilisation', 'Destruction', 'Desynchronisation', 'Failure',
                       'Dereferencing', 'Overflow', 'Underflow', 'NMI', 'Interrupt', 'Corruption', 'Anomoly',
                       'Seizure', 'Override', 'Reclock', 'Rejection', 'Invalidation', 'Halt', 'Exhaustion',
                       'Infection', 'Incompatibility', 'Timeout', 'Expiry', 'Unavailability', 'Bug', 'Condition',
                       'Crash', 'Dump', 'Crashdump', 'Stackdump', 'Problem', 'Lockout']

    fourth_word_list = ['Error', 'Problem', 'Warning', 'Signal', 'Flag']

    # will run forever until you say no
    while True:
        # pick random word from list
        word_from_list1 = first_word_list[random.randint(0, 53)]
        word_from_list2 = second_word_list[random.randint(0, 53)]
        word_from_list3 = third_word_list[random.randint(0, 31)]
        optional_is_true = random.randint(0, 1)  # Is 4th list needed?
        word_from_list4 = fourth_word_list[random.randint(0, 4)]
        core_excuse = f'{word_from_list1} {word_from_list2} {word_from_list3}'
        # prompt for loop
        yes_or_no = input('Do you want an excuse? Yes or No\n').lower()
        # deciding factor of loop
        if yes_or_no[0] == 'y':
            if optional_is_true:
                print(f'{core_excuse} {word_from_list4}\n')
            else:
                print(f'{core_excuse}\n')
        else:
            break


if __name__ == '__main__':
    main()
