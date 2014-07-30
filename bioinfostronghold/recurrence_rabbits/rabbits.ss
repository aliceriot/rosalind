#lang scheme

(define rabbits
  (lambda (n k rn1 rn2)
    (cond
      ((eq? n 0) 0)
      (else
        (+ rn1 (rabbits (sub1 n) k (+ rn1 (* k rn2)) rn1))))))

;; I made an implementation that works in python, I think it would be fun to make the same thing work in Scheme too

(define rabbits
  (lambda (n k step)
    (cond
      ((eq? step n)(quote()))
      ((eq? step 1)
       (cons (cons 1 1)(rabbits n k (+ 1 step))))

;;I don't know how to address arrays and things like that in scheme, so I'm not sure how to go about doing this


