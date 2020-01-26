import random
from collections import defaultdict

fail = [True, None]
def is_pattern_segment(pattern):
    return pattern.startswith('?*') and all(a.isalpha() for a in pattern[2:])

def segment_match(pattern, saying):
    seg_pat, rest = pattern[0], pattern[1:]
    seg_pat = seg_pat.replace('?*', '?')
    if not rest: return (seg_pat, saying), len(saying)    
    for i, token in enumerate(saying):
        if rest[0] == token and is_match(rest[1:], saying[(i + 1):]):
            return (seg_pat, saying[:i]), i
    return (seg_pat, saying), len(saying)

def is_match(rest, saying):
    if not rest and not saying:
        return True
    if not all(a.isalpha() for a in rest[0]):
        return True
    if rest[0] != saying[0]:
        return False
    return is_match(rest[1:], saying[1:])

def pat_match_with_seg(pattern, saying):
    if not pattern or not saying: return []
    pat = pattern[0]
    if is_pattern_segment(pat):
        match, index = segment_match(pattern, saying)
        return [match] + pat_match_with_seg(pattern[1:], saying[index:])
    elif pat == saying[0]:
        return pat_match_with_seg(pattern[1:], saying[1:])
    else:
        return fail
        
def find_key_for_patterns(pattern, saying): 
    if not pattern or not saying: return 0
    else:
        pat = pattern[0]
        if is_pattern_segment(pat):
            match, index = segment_match(pattern, saying)
            return 1 + find_key_for_patterns(pattern[1:], saying[index:])
        else:
            if pat != saying[0]: return -999
            else: return find_key_for_patterns(pattern[1:], saying[1:])
    
def pat_to_dict(patterns):
    return {k: ' '.join(v) if isinstance(v, list) else v for k, v in patterns}

def subsitite(rule, parsed_rules):
    if not rule: return []
    return [parsed_rules.get(rule[0], rule[0])] + subsitite(rule[1:], parsed_rules)

def get_response(saying,rules):
    for key in rules:  
        if find_key_for_patterns(key.split(),saying.split())==key.count("?"):
            variable_match = pat_match_with_seg(key.split(),saying.split())
            choice = random.choice
            answer_rule = rules[key][random.choice(range(len(rules[key])))]
            print('Chatbot: ' + ' '.join(subsitite(answer_rule.split(), pat_to_dict(variable_match))))
            print('\n')
            
defined_patterns = {
    '?*x hello ?*y': ['?y', 'Please state your problem, ?x'],
    '?*x I want ?*y': ['What would it mean if you got ?y', 'Why do you want ?y', 'Suppose you got ?y soon'],
    '?*x if ?*y': ['Do you really think its likely that ?y', 'Do you wish that ?y', 'What do you think about ?y', 'Really-- if ?y'],
    '?*x no ?*y': ['Why not?', 'You are being a negative', 'Are you saying \'No\' just to be negative?'],
    '?*x I was ?*y': ['Were you really ?y ?', 'Perhaps I already knew you were ?y', 'Why do you tell me you were ?y now?'],
    '?*x I feel ?*y': ['Do you often feel ?y ?', 'What other feelings do you have?']
}
get_response("Tom hello How are you?",defined_patterns)
get_response("I was busy this weekend",defined_patterns)
get_response("Tom I want this box",defined_patterns)
get_response("There is no ball",defined_patterns)
get_response("Hey I feel interesting",defined_patterns)