#input 
#sentence = input('input kalimat : ') 
#from tkinter import FALSE, TRUE


def parser(sentence):
  tokens = sentence.lower().split() 
  tokens.append('EOS') 

  #symbol 
  non_terminals = ['S','NN','VB'] 
  terminals=['ulun','ikam','amang','wadai','iwak','ading','abah','maigut','mamakan','manatak'] 
  
  #parse table 
  parse_table ={} 
  
  parse_table[('S', 'ulun')] = ['NN','VB','NN'] 
  parse_table[('S', 'ikam')] = ['NN','VB','NN'] 
  parse_table[('S', 'amang')] = ['NN','VB','NN'] 
  parse_table[('S', 'wadai')] = ['NN','VB','NN'] 
  parse_table[('S', 'iwak')] = ['NN','VB','NN'] 
  parse_table[('S', 'ading')] = ['NN','VB','NN'] 
  parse_table[('S', 'abah')] = ['NN','VB','NN'] 
  parse_table[('S', 'maigut')] = ['error'] 
  parse_table[('S', 'mamakan')] = ['error'] 
  parse_table[('S', 'manatak')] = ['error'] 
  parse_table[('S', 'EOS')] = ['error'] 
  
  parse_table[('NN', 'ulun')] = ['ulun'] 
  parse_table[('NN', 'ikam')] = ['ikam'] 
  parse_table[('NN', 'amang')] = ['amang'] 
  parse_table[('NN', 'wadai')] = ['wadai'] 
  parse_table[('NN', 'iwak')] = ['iwak']
  parse_table[('NN', 'ading')] = ['ading'] 
  parse_table[('NN', 'abah')] = ['abah'] 
  parse_table[('NN', 'maigut')] = ['error'] 
  parse_table[('NN', 'mamakan')] = ['error'] 
  parse_table[('NN', 'manatak')] = ['error'] 
  parse_table[('NN', 'EOS')] = ['error'] 
  
  parse_table[('VB', 'ulun')] = ['error'] 
  parse_table[('VB', 'ikam')] = ['error'] 
  parse_table[('VB', 'amang')] = ['error'] 
  parse_table[('VB', 'wadai')] = ['error'] 
  parse_table[('VB', 'iwak')] = ['error'] 
  parse_table[('VB', 'ading')] = ['error'] 
  parse_table[('VB', 'abah')] = ['error'] 
  parse_table[('VB', 'maigut')] = ['maigut'] 
  parse_table[('VB', 'mamakan')] = ['mamakan'] 
  parse_table[('VB', 'manatak')] = ['manatak'] 
  parse_table[('NN', 'EOS')] = ['error'] 

  # stack initialization 
  stack = [] 
  stack.append('#') 
  stack.append('S') 

  # input reading initialization
  idx_token = 0
  symbol = tokens[idx_token]
  
  #
  while (len(stack) > 0):
    top = stack [len(stack) - 1]
    if top in terminals:
      if top == symbol:
        stack.pop()
        idx_token = idx_token + 1
        symbol = tokens[idx_token]
        if symbol == 'EOS':
          stack.pop()
      else:
        print('error')
        break;
    elif top in non_terminals:
      if parse_table[(top, symbol)][0] != 'error':
          stack.pop()
          symbols_to_be_pushed = parse_table[(top, symbol)]
          for i in range(len(symbols_to_be_pushed)-1,-1,-1):
              stack.append(symbols_to_be_pushed[i])
      else:
          print('error')
          break;
    else:
      print('error')
      break;
  print()
  
  # conclusion 
  print() 
  if symbol == 'EOS' and len(stack) == 0: 
      print('Input string ', sentence, ' diterima, sesuai Grammar') 
      return True
  else: 
      print('Error, input string: ', sentence, ', tidak diterima, tidak sesuai Grammar') 
      return False
