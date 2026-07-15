### Проверить ипотечный калькулятор на 4 случаях: обычная ставка, 0%, отрицательная сумма, нулевой срок.

500,000 3.86 25 

```ssh
Your principal:	 $500,000.00
Your rate:		 3.86%
Your term:		 25 years
Your payment:	 $2,600.69
```

500,000 0 25 ->

```ssh
Your principal:	 $500,000.00
Your rate:		 0.00%
Your term:		 25 years
Your payment:	 $1,666.67
```

-500,000 3.86 25
```ssh
Input principal $: -500000
Input annual rate %: 3.86
Input term in years: 25
principal, and years should be > 0, annual_rate should be not < 0
```

500,000 3.86 0
```ssh
Input principal $: 500000
Input annual rate %: 3.86
Input term in years: 0
principal, and years should be > 0, annual_rate should be not < 0
```
