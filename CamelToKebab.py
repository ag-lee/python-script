import inflection
import pyperclip

print('==== Start Program ====')

while 1:
	x = raw_input()
	if x == 'q':
		break;
	
	x = x.replace('.do','')
	x = inflection.dasherize(inflection.underscore(x));
	pyperclip.copy(x)
	print(x)

print('==== End Program ====')

