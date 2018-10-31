(defun split-str (str sep)
  (let ((i (search sep str)))
    (if (null i)
      (vector str)
      (concatenate 'vector
                   (vector (subseq str 0 i))
                   (split-str (subseq str (+ i (length sep))) sep)))))

(defun int-range (str)
  (let ((parts (split-str str ",")))
    (vector (parse-integer (elt parts 0))
            (parse-integer (elt parts 1)))))

(defun parse (line)
  (let ((words (split-str line " ")))
    (cond ((equal (elt words 0) "toggle")
           (vector 'toggle
                   (int-range (elt words 1))
                   (int-range (elt words 3))))
          ((equal (elt words 1) "off")
           (vector 'off
                   (int-range (elt words 2))
                   (int-range (elt words 4))))
          ((equal (elt words 1) "on")
           (vector 'on
                   (int-range (elt words 2))
                   (int-range (elt words 4)))))))

(defun read-lines ()
  (let ((line (read-line nil nil)))
    (if (> (length line) 0) (cons line (read-lines)) nil)))

(defun count-bulbs (instructions updater)
  (let ((lights (make-array '(1000 1000) :initial-element 0)))
    (dotimes (i (length instructions))
      (let* ((instruction (elt instructions i))
             (command (elt instruction 0))
             (startx (elt (elt instruction 1) 0))
             (starty (elt (elt instruction 1) 1))
             (endx (elt (elt instruction 2) 0))
             (endy (elt (elt instruction 2) 1)))
        (loop for x from startx to endx do
              (loop for y from starty to endy do
                    (setf (aref lights x y)
                          (funcall updater command (aref lights x y)))))))
    (reduce #'+ (make-array (array-total-size lights) :displaced-to lights))))

(defun sol-1 (instructions)
  (count-bulbs instructions
               (lambda (command n)
                 (case command
                   ('off 0)
                   ('on 1)
                   ('toggle (logxor n 1))))))

(defun sol-2 (instructions)
  (count-bulbs instructions
               (lambda (command n)
                 (case command
                   ('off (max 0 (- n 1)))
                   ('on (+ n 1))
                   ('toggle (+ n 2))))))

(setf instructions (mapcar #'parse (read-lines)))

(print (sol-1 instructions))
(print (sol-2 instructions))
