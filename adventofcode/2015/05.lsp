(defun nice-string-p (str)
  (and
    (let ((numvowels 0))
      (dotimes (i (length str) nil)
        (and (member (elt str i) '(#\a #\e #\i #\o #\u)) (incf numvowels))
        (if (>= numvowels 3)
          (return t))))
    (dotimes (i (- (length str) 1) nil)
      (if (eq (elt str i) (elt str (+ i 1)))
        (return t)))
    (dotimes (i (- (length str) 1) t)
      (if (member (subseq str i (+ i 2)) '("ab" "cd" "pq" "xy") :test #'string=)
        (return nil)))))

(defun nice-string2-p (str)
  (and
    (dotimes (i (- (length str) 1) nil)
      (if (search (subseq str i (+ i 2)) (subseq str (+ i 2)))
        (return t)))
    (dotimes (i (- (length str) 2) nil)
      (if (eq (elt str i) (elt str (+ i 2)))
        (return t)))))

(defun read-lines ()
  (let ((line (read-line nil nil)))
    (if (> (length line) 0) (cons line (read-lines)) nil)))

(defun sol-1 (lines)
  (length (remove-if-not #'nice-string-p lines)))

(defun sol-2 (lines)
  (length (remove-if-not #'nice-string2-p lines)))

(setf lines (read-lines))

(print (sol-1 lines))
(print (sol-2 lines))
