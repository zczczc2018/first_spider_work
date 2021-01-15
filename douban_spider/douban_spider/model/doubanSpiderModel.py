from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from config import SQLALCHEMY_DATABASE_URI, POOL_SIZE, MAX_OVERFLOW
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
Base = declarative_base()


def get_mysql_engine():
    engine = create_engine(SQLALCHEMY_DATABASE_URI,
                           pool_size=POOL_SIZE,
                           max_overflow=MAX_OVERFLOW,
                           pool_recycle=7200
                           )
    return engine


def get_mysql_session(engine):
    session = scoped_session(sessionmaker(bind=engine))
    return session


class DoubanMovie(Base):
    __tablename__ = 'movies'
    movie_name = Column(String(255), primary_key=True)
    director = Column(String(255))
    scriptwriter = Column(String(255))
    actors = Column(String(4000))
    rating = Column(String(20))
    movie_type = Column(String(255))
    movie_country = Column(String(255))
    language = Column(String(255))
    play_date = Column(String(255))
    movie_length = Column(String(50))
    other_name = Column(String(255))

    @classmethod
    def add_movie_info(cls, **kwargs):
        engine = get_mysql_engine()
        session = get_mysql_session(engine)
        try:
            filter_list = []
            filter_list.append(cls.movie_name==kwargs.get('movie_name'))
            contactinfo_model = session.query(cls.movie_name).filter(*filter_list)
            if contactinfo_model.first():
                contactinfo_model.update(kwargs)
                print('更新成功')
            else:
                contactinfo_model = DoubanMovie(
                    movie_name=kwargs.get('movie_name'),
                    director=kwargs.get('director'),
                    scriptwriter=kwargs.get('scriptwriter'),
                    actors=kwargs.get('actors'),
                    rating=kwargs.get('rating'),
                    movie_type=kwargs.get('movie_type'),
                    movie_country=kwargs.get('movie_country'),
                    language=kwargs.get('language'),
                    play_date=kwargs.get('play_date'),
                    movie_length=kwargs.get('movie_length'),
                    other_name=kwargs.get('other_name')
                )
                session.add(contactinfo_model)
                print("新增数据成功")
            session.commit()
        except Exception as e:
            session.rollback()
            print('数据库异常，更新失败')
            return {'message': '数据库异常，更新失败', 'error': e.args}
        finally:
            engine.dispose()
            session.remove()
        return {'message': 'OK'}