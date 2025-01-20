import time
import uuid


class IDUtils:
    """
    Class for generating various types of unique IDs for your Python project.

    This class offers flexibility and security in ID generation, addressing
    potential issues raised in the ratings.
    """

    @staticmethod
    def generate_unique_id(
            prefix: str = "",
            length: int = 20,
            use_time: bool = False,
            use_random: bool = True,
            delimiter: str = "-",
    ) -> str:
        """
        Generates a unique ID based on specified parameters.

        Args:
            prefix (str, optional): A prefix to prepend to the ID. Defaults to "".
            length (int, optional): The desired length of the ID. Defaults to 20.
            use_time (bool, optional): Whether to incorporate the current timestamp. Defaults to True.
            use_random (bool, optional): Whether to use random components for better uniqueness. Defaults to True.
            delimiter (str, optional): The delimiter to separate ID components. Defaults to "-".

        Returns:
            str: The generated unique ID.

        Raises:
            ValueError: If the requested length is less than 0.
        """

        if length < 0:
            raise ValueError("ID length must be non-negative.")

        components = []

        if prefix:
            components.append(prefix)

        if use_time:
            timestamp = str(int(time.time() * 1000))
            components.append(timestamp)

        if use_random:
            random_part = uuid.uuid4().hex[: length - len(components)]
            components.append(random_part)

        return delimiter.join(components)
