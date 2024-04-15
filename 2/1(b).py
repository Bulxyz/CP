To determine the decimal values for the biased exponent ( e ) and the true exponent ( p ):

Biased Exponent ( e ) (decimal value):

We have previously calculated the biased exponent as 10001111 in binary.
To convert this binary value to decimal, we consider it as a signed binary number:
The given binary number is negative because the most significant bit is 1.
Convert the magnitude of the positive binary number to decimal: 00...01111.
The decimal value of 00001111 is 15.
Since the sign is negative, the biased exponent value (e) is -(15) = -15.
True Exponent ( p ) (decimal value):

The true exponent ( p ) can be calculated by adjusting for the bias (127) used in single-precision floating-point representation.
To find the true exponent (( p )), we subtract the bias from the biased exponent ( e ):
True exponent ( p ) = Biased exponent ( e ) - Bias
True exponent ( p ) = -15 - 127
True exponent ( p ) = -142.
Therefore, the decimal value for the biased exponent ( e ) is -15, and the decimal value for the true exponent ( p ) is -142.

