from enum import Enum


class StudentGradeEnum(Enum):
    """
    An enumeration representing the various grades a student can be classified into.

    This enumeration is used to define all possible grade levels a student might belong
    to, starting from pre-kindergarten to grade 12. The purpose of this class is to
    provide a standard and structured way of referencing and handling student grade levels.

    Attributes:
        PRE_KG (str): Represents the grade level for pre-kindergarten students.
        KG (str): Represents the grade level for kindergarten students.
        UKG (str): Represents the grade level for upper kindergarten students.
        LKG (str): Represents the grade level for lower kindergarten students.
        GRADE_1 (str): Represents the grade level for students in grade 1.
        GRADE_2 (str): Represents the grade level for students in grade 2.
        GRADE_3 (str): Represents the grade level for students in grade 3.
        GRADE_4 (str): Represents the grade level for students in grade 4.
        GRADE_5 (str): Represents the grade level for students in grade 5.
        GRADE_6 (str): Represents the grade level for students in grade 6.
        GRADE_7 (str): Represents the grade level for students in grade 7.
        GRADE_8 (str): Represents the grade level for students in grade 8.
        GRADE_9 (str): Represents the grade level for students in grade 9.
        GRADE_10 (str): Represents the grade level for students in grade 10.
        GRADE_11 (str): Represents the grade level for students in grade 11.
        GRADE_12 (str): Represents the grade level for students in grade 12.
    """
    PRE_KG = "PRE_KG"
    KG = "KG"
    UKG = "UKG"
    LKG = "LKG"
    GRADE_1 = "1"
    GRADE_2 = "2"
    GRADE_3 = "3"
    GRADE_4 = "4"
    GRADE_5 = "5"
    GRADE_6 = "6"
    GRADE_7 = "7"
    GRADE_8 = "8"
    GRADE_9 = "9"
    GRADE_10 = "10"
    GRADE_11 = "11"
    GRADE_12 = "12"

    def is_elementary(self) -> bool:
        """
        Check if the grade level is considered an elementary grade level.

        Returns:
            bool: True if the grade level is elementary, False otherwise.
        """
        return self in {self.PRE_KG, self.KG, self.UKG, self.LKG, self.GRADE_1, self.GRADE_2, self.GRADE_3,
                        self.GRADE_4, self.GRADE_5}

    def is_middle(self) -> bool:
        """
        Check if the grade level is considered a middle school grade level.

        Returns:
            bool: True if the grade level is middle school, False otherwise.
        """
        return self in {self.GRADE_6, self.GRADE_7, self.GRADE_8}

    def is_high(self) -> bool:
        """
        Check if the grade level is considered a high school grade level.

        Returns:
            bool: True if the grade level is high school, False otherwise.
        """
        return self in {self.GRADE_9, self.GRADE_10, self.GRADE_11, self.GRADE_12}
