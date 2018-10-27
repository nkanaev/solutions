; utility

(defun split-by-char (ch str)
  (let ((pos (position ch str)))
    (if (null pos)
      (list str)
      (cons (subseq str 0 pos) (split-by-char ch (subseq str (+ pos 1)))))))

(defun read-lines ()
  (let ((line (read-line nil nil)))
    (if (> (length line) 0) (cons line (read-lines)) nil)))

; solution

(defun paper-needed (l w h)
  (let ((s1 (* l w))
        (s2 (* l h))
        (s3 (* w h)))
    (+ (* 2 (+ s1 s2 s3)) (min s1 s2 s3))))

(defun ribbon-needed (l w h)
  (let ((s (sort (list l w h) #'<)))
    (+ (* 2 (+ (car s) (cadr s))) (* l w h))))

(defun sol-1 (sizes)
  (reduce #'+ (mapcar #'(lambda (s) (apply #'paper-needed s)) sizes)))

(defun sol-2 (sizes)
  (reduce #'+ (mapcar #'(lambda (s) (apply #'ribbon-needed s)) sizes)))

; input & result

(setf
  sizes
  (mapcar
    #'(lambda (line) (mapcar #'parse-integer (split-by-char #\x line)))
    (read-lines)))

(print (sol-1 sizes))
(print (sol-2 sizes))
