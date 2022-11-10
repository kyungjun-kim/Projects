// Scala 기초 문법 공부

// Hello, world!
object LearnScala {
    def main(args: Array[String]): Unit = {
        println("Hello, world!")
    }
}
/* object를 통해 객체 생성, def를 통해 함수 생성
자바와 비슷하면서도 다르다
*/

// 변수 & 계산
object LearnScala {
    def main(args: Array[String]): Unit = {
        println( 1 + 2 )
        println( (1).+(3) )
    }
}

/* 스칼라에선 원시 타입 (ex 1(Int 리터럴))은 객체로 취급
그래서 "+", "-" 와 같은 연산자는 1이라는 원시 타입 객체의 메소드
ex) 1+2 는 1이라는 객체에 "+"라는 메소드를 호출해 2라는 인자가 전달되는 것
*/


// 변수 & 상수
object LearnScala {
    def main(args: Array[String]): Unit = {
        var x = 1 + 2
        x = 3 * 4
        println( x )
        
        val y = 1 + 2
        y = 3 * 4 // 이 줄은 상수에 값을 대입해서 에러가 나기 때문에 지워야 합니다.
        println( y )
        
        // 한 번에 여러개의 변수를 선언하면서 값을 대입할 수도 있습니다.
        var a, b, c = 5
        println( a )
        println( b )
        println( c )
    }
}
/* 변수는 var로, 상수는 val로 선언 
한번에 여러 개의 변수 선언을 하고 값을 대입하는 것도 가능
*/