01.out: 01.c
	@cc -g 01.c -o 01.out

02.out: 02.c
	@cc -g 02.c -o 02.out

03.out: 03.c
	@cc -g 03.c -o 03.out

04.out: 04.c
	@cc -g 04.c -o 04.out

05.out: 05.c
	@cc -g 05.c -o 05.out

sol01: 01.out
	@./01.out < 01.txt

sol02: 02.out
	@./02.out < 02.txt

sol03: 03.out
	@./03.out < 03.txt

sol04: 04.out
	@./04.out < 04.txt

sol05: 05.out
	@./05.out < 05.txt

clean:
	@rm -r *.out *.dSYM/
