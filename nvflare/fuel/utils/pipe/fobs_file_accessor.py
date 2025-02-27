# Copyright (c) 2023, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Any

from nvflare.fuel.utils import fobs

from .file_accessor import FileAccessor


class FobsFileAccessor(FileAccessor):
    def read(self, file_path: str) -> Any:
        """Read the file as a binary file and decode it with FOBS.

        Args:
            file_path: path to the file to be read

        Returns:

        """
        with open(file_path, mode="rb") as file:  # b is important -> binary
            data = file.read()
        return fobs.loads(data)

    def write(self, data: Any, file_path):
        """Write the data as binary file.

        Args:
            data: data to be written
            file_path: path of the file

        Returns:

        """
        data = fobs.dumps(data)
        with open(file_path, "wb") as f:
            f.write(data)
