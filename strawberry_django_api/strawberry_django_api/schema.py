from strawberry_django.optimizer import DjangoOptimizerExtension
import strawberry
from .models import File
from django.core.files.base import ContentFile
from strawberry.file_uploads import Upload
from typing import List


@strawberry.type
class FileType:
    id: int
    name: str
    file_url: str

@strawberry.type
class Mutation:
    @strawberry.mutation
    def upload_file(self, file: Upload) -> FileType:


        content_file = ContentFile(file.read())  
        content_file.name = file.name  
        
        file = File.objects.create(name=file.name)
        file.file.save(file.name, content_file)  
        
        return FileType(id=file.id, name=file.name, file_url=file.file.url)


@strawberry.type
class Query:
    @strawberry.field
    def files(self) -> List[FileType]:
        return [
            FileType(id=file.id, name=file.name, file_url=file.file.url)
            for file in File.objects.all()
        ]

schema = strawberry.federation.Schema(
  mutation=Mutation,
  query=Query,
  enable_federation_2=True,
  extensions=[
      DjangoOptimizerExtension, 
    ]
  )